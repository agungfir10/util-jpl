import cities from "./data/DATA_WILAYAH_PENERIMA_TAMBAHAN_2.json" assert { type: "json" };
import { mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path =
  "E:\\DOKUMEN TAMBAHAN 2 JATENG\\DOKUMEN NOVEMBER TAMBAHAN 2\\KOTA TEGAL";

let counter = 0;
cities.forEach((city) => {
  if (city.KOTA === "KOTA TEGAL") {
    mkdirSync(join(path, `${city.KOTA}-${city.KECAMATAN}-${city.DESA}`));
    counter++;
  }
});
console.log(counter);
