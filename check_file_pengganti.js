import fs from "fs";
import { join } from "path";
import dtt from "./data/DES_REG.json" assert { type: "json" };
import chalk from "chalk";

const path = "E:\\DOKUMEN OKTOBER JATENG\\KAB. TEGAL";

const folders = fs.readdirSync(path);

dtt.forEach((d) => {
  if (d.KOTA === "KAB. TEGAL") {
    try {
      fs.accessSync(
        join(path, `${d.KOTA}-${d.KECAMATAN}-${d.DESA}`, "PENGGANTI.pdf")
      );
      console.log(chalk.white.bgGreen(d.KOTA, d.KECAMATAN, d.DESA));
    } catch (e) {
      console.log(chalk.white.bgRed(d.KOTA, d.KECAMATAN, d.DESA));
    }
  }
});
