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
import dtt from "./data/DES_REG_UPLOAD.json" assert { type: "json" };
import { formatDate } from "./const.js";
import chalk from "chalk";
import { argv } from 'process'

// argv[2] = ALOKASI
// argv[3] = KETERANGAN (REG, +1, +2, +3)
// argv[4] = JENIS DOKUMEN

if (argv.length < 6) {
  throw new Error('Argumen kurang lengkap!')
}

const alokasi = getAlokasi(argv[2]);
const keterangan = getKeteranganAlokasi(argv[3]);
const typeUpload = getDocumentType(argv[4]);
const pathFolder = checkFolderPath(argv[5]);

// const typeFileString = "DTT";
// const alokasiString = "DES";
// const pathUploaded = join(
//   "./data",
//   `UPLOADED_${typeUploadString}_${alokasi}.txt`
// );
// const pathIndex = join(
//   "cache",
//   `${pathFolder
//     .replaceAll("\\", "-")
//     .replaceAll(":", "")}-${typeUploadString}-index.txt`
// );

// let index = 0;
// try {
//   accessSync(pathIndex);
//   index = Number(readFileSync(pathIndex));
// } catch (e) {
//   writeFileSync(pathIndex, "0");
//   index = Number(readFileSync(pathIndex));
// }

// function uploadDtt() {
//   if (index < dtt.length) {
//     const { NO_DTT, TANGGAL, KOTA, KECAMATAN, DESA } = dtt[index];
//     const tanggal = TANGGAL.split("/")[1];
//     const date = new Date(`12-${tanggal}-2023`);
//     if (checkFolderExists(join(pathFolder, `${KOTA}-${KECAMATAN}-${DESA}`))) {
//       if (
//         checkFolderExists(
//           join(
//             pathFolder,
//             `${KOTA}-${KECAMATAN}-${DESA}`,
//             `${typeFileString}.pdf`
//           )
//         )
//       ) {
//         const tanggalFormated = formatDate(date);
//         const form = new FormData();
//         form.append(
//           "file",
//           createReadStream(
//             join(
//               pathFolder,
//               `${KOTA}-${KECAMATAN}-${DESA}`,
//               `${typeFileString}.pdf`
//             )
//           )
//         );
//         form.append("userid", "GD11040101");
//         form.append("tanggal", tanggalFormated);
//         form.append("nodoc", NO_DTT);
//         form.append("jenis", typeUpload);
//         form.append("kdkantor", "11001");
//         const headers = form.getHeaders();
//         const req = https.request(
//           {
//             hostname: "astridjplb.id",
//             path: "/w/proc/proses_simpan_dokumen.php",
//             method: "POST",
//             headers: headers,
//           },
//           (res) => {
//             let response = "";
//             res.on("data", (chunk) => {
//               response += chunk.toString();
//             });
//             res.on("end", () => {
//               if (response === "1") {
//                 const date = formatDate(new Date());
//                 console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
//                 console.log(chalk.white.bgGreen("SUKSES"));
//                 writeLog(`${KOTA}-${KECAMATAN}-${DESA}|SUKSES|${date}`);
//                 updateIndex(index);
//                 index++;
//                 uploadDtt();
//               } else if (response.includes("|")) {
//                 console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
//                 console.log(
//                   chalk.black.bgYellow("DOKUMEN SUDAH DI UPLOAD"),
//                   response,
//                   `${KOTA}-${KECAMATAN}-${DESA}`
//                 );
//                 writeLog(`${KOTA}-${KECAMATAN}-${DESA}|${response}`);
//                 updateIndex(index);
//                 index++;
//                 uploadDtt();
//               } else {
//                 uploadDtt();
//                 console.log(response);
//                 console.log(chalk.white.bgRed('"GAGAL"'), "CEK UKURAN BERKAS");
//               }
//             });
//           }
//         );
//         req.on("error", (error) => {
//           console.log(error);
//           uploadDtt();
//         });
//         form.pipe(req);
//       } else {
//         writeLog(
//           `${KOTA}-${KECAMATAN}-${DESA}|BERKAS TIDAK ADA|${formatDate(
//             new Date()
//           )}`
//         );
//         index++;
//         uploadDtt();
//       }
//     } else {
//       index++;
//       uploadDtt();
//     }
//   } else {
//     console.log("Selesai...");
//   }
// }

// function updateIndex(index) {
//   writeFileSync(pathIndex, index.toString());
// }

// function writeLog(text) {
//   appendFileSync(pathUploaded, text + "\n");
// }

// if (pathFolder.includes(alokasiString)) {
//   uploadDtt();
// } else {
//   console.log(chalk.white.bgRed("Nama folder dan alokasi salah!"));
// }

function checkFolderExists(path) {
  try {
    accessSync(path);
    return true;
  } catch (e) {
    return false;
  }
}

function checkFolderPath(folder) {
  try {
    accessSync(folder)
  } catch (e) {
    throw new Error('Folder tidak ditemukan!')
  }

}
// function downloadDataDokumen() { }

function getAlokasi(alokasi) {
  if (alokasi === 'SEP') {
    return 'SEP'
  } else if (alokasi === 'OKT') {
    return 'OKT'
  } else if (alokasi === 'NOV') {
    return 'NOV'
  } else if (alokasi === 'DES') {
    return 'DES'
  } else {
    throw new Error('Alokasi salah!')
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
