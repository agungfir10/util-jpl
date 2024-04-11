import dtt from "./data/OKT_TAMBAHAN_2.json" assert { type: "json" };
import tanggal from "./data/TANGGAL_SEP_TAMBAHAN_2.json" assert { type: "json" };
import fs from "fs";

// tanggal.forEach((d) => {
//   if (d.TANGGAL === undefined) {
//     console.log("HELLO ");
//   }
// });

let newDtt = [];

let cocok = false;

dtt.forEach((d) => {
  for (let i = 0; i < tanggal.length; i++) {
    const t = tanggal[i];

    if (d.KOTA === t.KOTA && d.KECAMATAN === t.KECAMATAN && t.DESA === d.DESA) {
      newDtt.push({ ...d, TANGGAL: t.TANGGAL });
      cocok = true;
      break;
    }
  }

  if (!cocok) {
    newDtt.push({ ...d });
    cocok = false;
  }
});

fs.writeFileSync("./data/OKT_TAMBAHAN_2_UPLOAD.json", JSON.stringify(newDtt));
