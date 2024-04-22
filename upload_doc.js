import FormData from "form-data";
import {
  accessSync,
  writeFileSync,
  readFileSync,
  createReadStream,
  appendFileSync,
  mkdirSync,
} from "fs";
import https from "https";
import { join } from "path";
import { formatDate, __dirname } from "./const.js";
import chalk from "chalk";
import { argv } from "process";
import cities from "./data/KAB_KOTA.json" assert { type: "json" };

if (argv.length < 6) {
  throw new Error("Argumen kurang lengkap!");
}

const alokasi = getAlokasi(argv[2]);
const keterangan = getKeteranganAlokasi(argv[3]);
const type = argv[4];
const docType = getDocumentType(type);
const path = argv[5];
checkFolderPath(path);

const kota = path.includes("/")
  ? path.split("/").pop()
  : path.split("\\").pop();
checkCity(kota);

const pathUploaded = join(
  "./data",
  `UPLOADED_${type}_${alokasi}_${keterangan}.txt`
);

const pathIndex = join(
  "cache",
  `${path.replaceAll("\\", "-").replaceAll(":", "")}-${type}-index.txt`
);
const dtt = JSON.parse(
  readFileSync(join(__dirname, "data", `${alokasi}_${keterangan}_UPLOAD.json`))
);

let index = 0;
try {
  accessSync(pathIndex);
  index = Number(readFileSync(pathIndex));
} catch (e) {
  writeFileSync(pathIndex, "0");
  index = Number(readFileSync(pathIndex));
}

function uploadDtt() {
  if (index < dtt.length) {
    const { NO_DTT, TANGGAL, KOTA, KECAMATAN, DESA } = dtt[index];
    const folder = `${KOTA}-${KECAMATAN}-${DESA}`;
    if (checkFolderExists(join(path, folder))) {
      const filepath = join(path, folder, `${type}.pdf`);
      if (checkFolderExists(filepath)) {
        const tanggalFormated = formatDate(new Date(TANGGAL));
        const form = new FormData();
        form.append("file", createReadStream(filepath));
        form.append("userid", "GD11040101");
        form.append("tanggal", tanggalFormated);
        form.append("nodoc", NO_DTT);
        form.append("jenis", docType);
        form.append("kdkantor", "11001");
        const headers = form.getHeaders();
        const req = https.request(
          {
            hostname: "astridjplb.id",
            path: "/w/proc/proses_simpan_dokumen.php",
            method: "POST",
            headers: headers,
          },
          (res) => {
            let response = "";
            res.on("data", (chunk) => {
              response += chunk.toString();
            });
            res.on("end", () => {
              if (response === "1") {
                const date = formatDate(new Date());
                console.log(folder);
                console.log(chalk.white.bgGreen("SUKSES"));
                writeLog(`${folder}|SUKSES|${date}`);
                updateIndex(index);
                index++;
                uploadDtt();
              } else if (response.includes("|")) {
                console.log(folder);
                console.log(
                  chalk.black.bgYellow("DOKUMEN SUDAH DI UPLOAD"),
                  response,
                  folder
                );
                writeLog(`${folder}|${response}`);
                updateIndex(index);
                index++;
                uploadDtt();
              } else {
                uploadDtt();
                console.log(response);
                console.log(chalk.white.bgRed('"GAGAL"'), "CEK UKURAN BERKAS");
              }
            });
          }
        );
        req.on("error", (error) => {
          console.log(error);
          uploadDtt();
        });
        form.pipe(req);
      } else {
        writeLog(
          `${KOTA}-${KECAMATAN}-${DESA}|BERKAS TIDAK ADA|${formatDate(
            new Date()
          )}`
        );
        index++;
        uploadDtt();
      }
    } else {
      index++;
      uploadDtt();
    }
  } else {
    console.log("Selesai...");
  }
}

function updateIndex(index) {
  writeFileSync(pathIndex, index.toString());
}

function writeLog(text) {
  try {
    accessSync(pathUploaded);
    appendFileSync(pathUploaded, text + "\n");
  } catch (e) {
    writeFileSync(pathUploaded, text + "\n");
  }
}

if (path.includes(alokasi)) {
  uploadDtt();
} else {
  console.log(chalk.white.bgRed("Nama folder dan alokasi salah!"));
}

function checkFolderExists(path) {
  try {
    accessSync(path);
    return true;
  } catch (e) {
    return false;
  }
}

function checkCity(city) {
  if (cities.includes(city)) {
    return;
  } else {
    throw new Error("Kota tidak ditemukan!");
  }
}

function checkFolderPath(folder) {
  try {
    accessSync(folder);
  } catch (e) {
    throw new Error("Folder tidak ditemukan!");
  }
}

function getAlokasi(alokasi) {
  const allAlokasi = ["SEP", "OKT", "NOV", "DES"];
  if (allAlokasi.includes(alokasi)) {
    return alokasi;
  } else {
    throw new Error("Alokasi salah!");
  }
}

function getKodeAlokasi(alokasi) {
  if (alokasi === "SEP") {
    return "21 | SEPTEMBER";
  } else if (alokasi === "OKT") {
    return "22 | OKTOBER";
  } else if (alokasi === "NOV") {
    return "23 | NOVEMBER";
  } else if (alokasi === "DES") {
    return "31 | DESEMBER";
  } else {
    throw new Error("Alokasi salah!");
  }
}
function getKeteranganAlokasi(keterangan) {
  if (keterangan === "REG") {
    return "REG";
  } else if (keterangan === "+1") {
    return "TAMBAHAN 1";
  } else if (keterangan === "+2") {
    return "TAMBAHAN 2";
  } else if (keterangan === "+3") {
    return "TAMBAHAN 3";
  } else {
    throw new Error("Keterangan alokasi salah!");
  }
}

function getDocumentType(type) {
  if (type === "DTT") {
    return "7 | DTT";
  } else if (type === "SPTJM") {
    return "9 | SPTJM (input nomor-DTT)";
  } else if (type === "PENGGANTI") {
    return "10 | BAST PENGGANTI (input nomor DTT)";
  } else if (type === "PERWAKILAN") {
    return "11 | BAST PERWAKILAN (input nomor DTT)";
  } else {
    throw new Error("Salah tipe dokumen...");
  }
}
