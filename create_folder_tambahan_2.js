import cities from "./data/DATA_WILAYAH_PENERIMA_TAMBAHAN_2.json" assert { type: "json" };
import { mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path =
  "/Users/agungfir/Downloads/KAB JEPARA TAMB 2 SEP";

let counter = 0;
cities.forEach((city) => {
  if (city.KOTA === "KAB. JEPARA") {
    mkdirSync(join(path, `${city.KOTA}-${city.KECAMATAN}-${city.DESA}`));
    counter++;
  }
});
console.log(counter);
