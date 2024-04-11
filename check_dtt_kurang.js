import fs from "fs";
import { join } from "path";
import dtt from "./data/DES_REG.json" assert { type: "json" };
import chalk from "chalk";

const path = "D:\\OKTOBER\\KARESIDENAN PATI\\KAB. REMBANG";

const folders = fs.readdirSync(path);

// folders.forEach((folder) => {
//   try {
//     fs.accessSync(join(path, folder, "DTT.pdf"));
//   } catch (e) {
//     console.log(folder, "TIDAK DIKETEMUKAN");
//   }
// });
dtt.forEach((d) => {
  if (d.KOTA === "KAB. REMBANG") {
    try {
      fs.accessSync(join(path, `${d.KOTA}-${d.KECAMATAN}-${d.DESA}`));
      console.log(chalk.white.bgGreen(d.KOTA, d.KECAMATAN, d.DESA));
    } catch (e) {
      console.log(chalk.white.bgRed(d.KOTA, d.KECAMATAN, d.DESA));
    }
  }
});
