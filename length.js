import dtt from "./DTT.json" assert { type: "json" };
import fs from "fs";

const files = fs.readdirSync("E:\\KC PATI\\DESEMBER\\DTT PDF");
let match = false;

console.log(dtt.length);

// dtt.forEach((d) => {
//   if (
//     d.KOTA === "KAB. BLORA" ||
//     d.KOTA === "KAB. JEPARA" ||
//     d.KOTA === "KAB. KUDUS" ||
//     d.KOTA === "KAB. PATI" ||
//     d.kota === "KAB. REMBANG"
//   ) {
//     for (let index = 0; index < files.length; index++) {
//       const no = files[index].split(".")[0];
//       if (d.NO === Number(no)) {
//         match = true;
//         break;
//       }
//     }
//     if (match === false) {
//       console.log(d.DESA);
//     }
//     match = false;
//   }
// });

// files.forEach((d) => {
//   for (let index = 0; index < dtt.length; index++) {
//     const no = d.split(".")[0];
//     const NO = dtt[index].NO;
//     if (Number(no) === NO) {
//       match = true;
//       break;
//     }
//   }
//   if (match === false) {
//     console.log(d);
//   }
//   match = false;
// });

const filter = dtt.filter((d) => d.TANGGAL === undefined || d.TANGGAL === "");

console.log(filter);
const date = new Date("7-12-2023");

console.log(date);

function formatDate(date) {
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();

  return `${year}-${month}-${day}`;
}

console.log(formatDate(date));
