import { accessSync, readdirSync } from "fs";
import { join } from "path";
import dtt from "./RESULT.json" assert { type: "json" };

const path = "E:\\DOKUMEN DESEMBER JATENG\\KAB. DEMAK";
const folders = readdirSync(join(path));

folders.forEach((folder) => {
  if (!dtt.includes(folder)) {
    console.log(folder);
  }
});
