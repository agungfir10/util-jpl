import cities from "./data/KAB_KOTA_JATENG.json" assert { type: "json" };
import { mkdirSync } from "fs";
import { __dirname } from "./const.js";
import { join } from "path";

const path = "E:\\DOKUMEN SEPTEMBER REGULER JATENG\\KAB. KENDAL";

let counter = 0;

cities.forEach((city) => {
  if (city.kota === "KAB. KENDAL") {
    mkdirSync(join(path, `${city.kota}-${city.kec}-${city.desa}`));
    counter++;
  }
});
console.log(counter);
