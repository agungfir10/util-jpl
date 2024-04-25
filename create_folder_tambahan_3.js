import cities from "./data/DATA_WILAYAH_PENERIMA_TAMBAHAN_3.json" assert { type: "json" };
import { mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path =
  "E:\\DOKUMEN TAMBAHAN 3 JATENG\\NOVEMBER\\KAB. DEMAK";

let counter = 0;
cities.forEach((city) => {
  if (city.KOTA === "KAB. DEMAK") {
    mkdirSync(join(path, `${city.KOTA}-${city.KECAMATAN}-${city.DESA}`));
    counter++;
  }
});
console.log(counter);
