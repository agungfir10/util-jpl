import cities from "./data/DATA_WILAYAH_PENERIMA_TAMBAHAN_1.json" assert { type: "json" };
import { accessSync, mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path =
  "E:\\DOKUMEN TAMBAHAN 1 JATENG\\DOKUMEN OKTOBER TAMBAHAN 1\\KAB. REMBANG";

let counter = 0;

cities.forEach((city) => {
  if (city.KOTA === "KAB. REMBANG") {
    try {
      accessSync(join(path, `${city.KOTA}-${city.KECAMATAN}-${city.DESA}`));
    } catch (e) {
      mkdirSync(join(path, `${city.KOTA}-${city.KECAMATAN}-${city.DESA}`));
      // console.log(e);
    }
    counter++;
  }
});
console.log(counter);
