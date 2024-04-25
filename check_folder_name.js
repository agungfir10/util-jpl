import cities from "./data/NOV_TAMBAHAN 1_UPLOAD.json" assert { type: "json" };
import { accessSync } from "fs";
import { join } from "path";

const path = "F:\\0000TAMB REMBANG\\TAMBAHAN PATI NOV\\KAB REMBANG +1";

let i=0
cities.forEach((city) => {
  const { KOTA, KECAMATAN, DESA } = city;
  if (KOTA === "KAB. REMBANG") {
    try {
      accessSync(join(path, `${KOTA}-${KECAMATAN}-${DESA}`));
      // console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
      i++
    } catch (e) {
      console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
    }
  }
});

console.log(i)