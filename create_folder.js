import cities from "./data/KAB_KOTA_JATENG.json" assert { type: "json" };
import { mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path = "E:\\DOKUMEN DESEMBER JATENG\\KOTA SEMARANG";

let counter = 0;

cities.forEach((city) => {
  if (city.kota === "KOTA SEMARANG") {
    mkdirSync(join(path, `${city.kota}-${city.kec}-${city.desa}`));
    counter++;
  }
});
console.log(counter);
