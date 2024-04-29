import cities from "./data/SEP_REG_UPLOAD.json" assert { type: "json" };
import { accessSync } from "fs";
import { join } from "path";

const path = "/Users/agungfir/Downloads/OKTOBER/KAB. SUKOHARJO";

let i = 0
cities.forEach((city) => {
  const { KOTA, KECAMATAN, DESA } = city;
  if (KOTA === "KAB. SUKOHARJO") {
    try {
      i++
      accessSync(join(path, `${KOTA}-${KECAMATAN}-${DESA}`));
      // console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
    } catch (e) {
      console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
    }
  }
});

console.log(i)