import cities from "./data/DATA_WILAYAH_PENERIMA_TAMBAHAN_2.json" assert { type: "json" };
import { mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path =
  "/Users/agungfir/Downloads/TAMBAHAN 2/SEPTEMBER/KAB. BLORA";

let counter = 0;
cities.forEach((city) => {
  if (city.KOTA === "KAB. BLORA") {
    mkdirSync(join(path, `${city.KOTA}-${city.KECAMATAN}-${city.DESA}`));
    counter++;
  }
});
console.log(counter);
