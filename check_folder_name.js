import cities from "./data/NOV_TAMBAHAN 3_UPLOAD.json" assert { type: "json" };
import { accessSync } from "fs";
import { join } from "path";

const path = "F:\\KAB DEMAK TAMBAHAN III\\NOV";

let i=0
cities.forEach((city) => {
  const { KOTA, KECAMATAN, DESA } = city;
  if (KOTA === "KAB. DEMAK") {
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