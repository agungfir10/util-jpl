import FormData from "form-data";
import fs from "fs";
import https from "https";
import path from "path";
import dtt from "./data/SEP_REG_UPLOAD.json" assert { type: "json" };
import { formatDate } from "./const.js";
import chalk from "chalk";

const pathFolder = process.argv[2];
const typeUpload = "10 | BAST PENGGANTI (input nomor DTT)";
const typeUploadString = "PENGGANTI";
const alokasi = "SEP_REG";
const pathUploaded = path.join(
  "./data",
  `UPLOADED_${typeUploadString}_${alokasi}.txt`
);
const pathIndex = path.join(
  "cache",
  `${pathFolder
    .replaceAll("\\", "-")
    .replaceAll(":", "")}-${typeUploadString}-index.txt`
);

let index = 0;
try {
  fs.accessSync(pathIndex);
  index = Number(fs.readFileSync(pathIndex));
} catch (e) {
  fs.writeFileSync(pathIndex, "0");
  index = Number(fs.readFileSync(pathIndex));
}

function uploadDtt() {
  if (index < dtt.length) {
    const { NO_DTT, TANGGAL, KOTA, KECAMATAN, DESA } = dtt[index];

    const tanggal = TANGGAL.split("/")[1];
    const date = new Date(`10-${tanggal}-2023`);
    try {
      fs.accessSync(path.join(pathFolder, `${KOTA}-${KECAMATAN}-${DESA}`));
      fs.accessSync(
        path.join(
          pathFolder,
          `${KOTA}-${KECAMATAN}-${DESA}`,
          `${typeUploadString}.pdf`
        )
      );
      console.log(KOTA, KECAMATAN, DESA);
      updateIndex(index);

      const tanggalFormated = formatDate(date);

      const form = new FormData();

      form.append(
        "file",
        fs.createReadStream(
          path.join(
            pathFolder,
            `${KOTA}-${KECAMATAN}-${DESA}`,
            `${typeUploadString}.pdf`
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
              console.log(chalk.white.bgGreen("SUKSES"), KOTA, KECAMATAN, DESA);
              fs.appendFileSync(
                pathUploaded,
                `${KOTA}-${KECAMATAN}-${DESA}|SUKSES|${formatDate(
                  new Date()
                )}\n`
              );
              index++;
              uploadDtt();
            } else if (response.includes("|")) {
              index++;
              uploadDtt();
              fs.appendFileSync(
                pathUploaded,
                `${KOTA}-${KECAMATAN}-${DESA}|${response}\n`
              );
              console.log(
                chalk.white.bgYellow("DOKUMEN SUDAH DI UPLOAD"),
                response,
                KOTA,
                KECAMATAN,
                DESA
              );
            } else {
              uploadDtt();
              console.log(response);
              console.log(
                chalk.white.bgRed('"GAGAL"'),
                "CEK UKURAN BERKAS",
                KOTA,
                KECAMATAN,
                DESA
              );
            }
          });
        }
      );
      req.on("error", (error) => {
        console.log(error);
        uploadDtt();
      });

      form.pipe(req);
    } catch (e) {
      index++;
      uploadDtt();
    }
  } else {
    console.log("Selesai...");
  }
}

function updateIndex(index) {
  fs.writeFileSync(pathIndex, index.toString());
}

uploadDtt();
