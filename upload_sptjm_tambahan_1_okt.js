import FormData from "form-data";
import {
  accessSync,
  writeFileSync,
  readFileSync,
  createReadStream,
  appendFileSync,
} from "fs";
import https from "https";
import { join } from "path";
import dtt from "./data/OKT_TAMBAHAN_1_UPLOAD.json" assert { type: "json" };
import { formatDate } from "./const.js";
import chalk from "chalk";

const pathFolder = process.argv[2];
const typeUpload = "9 | SPTJM (input nomor-DTT)";
const typeUploadString = "SPTJM";
const typeFileString = "SPTJM";
const alokasi = "OKT_TAMBAHAN_1";
const alokasiString = "OKT";
const pathUploaded = join(
  "./data",
  `UPLOADED_${typeUploadString}_${alokasi}.txt`
);
const pathIndex = join(
  "cache",
  `${pathFolder
    .replaceAll("\\", "-")
    .replaceAll(":", "")}-${typeUploadString}-index.txt`
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
    const tanggal = TANGGAL.split("/")[1];
    const date = new Date(`12-${tanggal}-2023`);
    if (checkFolderExists(join(pathFolder, `${KOTA}-${KECAMATAN}-${DESA}`))) {
      if (
        checkFolderExists(
          join(
            pathFolder,
            `${KOTA}-${KECAMATAN}-${DESA}`,
            `${typeFileString}.pdf`
          )
        )
      ) {
        const tanggalFormated = formatDate(date);
        const form = new FormData();
        form.append(
          "file",
          createReadStream(
            join(
              pathFolder,
              `${KOTA}-${KECAMATAN}-${DESA}`,
              `${typeFileString}.pdf`
            )
          )
        );
        form.append("userid", "GD11040101");
        form.append("tanggal", tanggalFormated);
        form.append("nodoc", NO_DTT);
        form.append("jenis", typeUpload);
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
                console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
                console.log(chalk.white.bgGreen("SUKSES"));
                writeLog(`${KOTA}-${KECAMATAN}-${DESA}|SUKSES|${date}`);
                updateIndex(index);
                index++;
                uploadDtt();
              } else if (response.includes("|")) {
                console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
                console.log(
                  chalk.black.bgYellow("DOKUMEN SUDAH DI UPLOAD"),
                  response,
                  `${KOTA}-${KECAMATAN}-${DESA}`
                );
                writeLog(`${KOTA}-${KECAMATAN}-${DESA}|${response}`);
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
  appendFileSync(pathUploaded, text + "\n");
}

if (pathFolder.includes(alokasiString)) {
  uploadDtt();
} else {
  console.log(chalk.white.bgRed("CHECK FOLDER DAN ALOKASI APAKAH SESUAI"));
}

function checkFolderExists(path) {
  try {
    accessSync(path);
    return true;
  } catch (e) {
    return false;
  }
}
