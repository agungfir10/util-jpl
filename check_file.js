import { readdirSync, accessSync, renameSync, rmdirSync } from "fs";
import { join } from "path";
import { naturalCompare } from "./const.js";

const path = "E:\\DOKUMEN TAMBAHAN 3 JATENG\\NOVEMBER\\KAB. DEMAK";

const folders = readdirSync(path).sort(naturalCompare);

folders.forEach((folder) => {
  // const files = readdirSync(join(path, folder));
  // if (files.length === 0) {
  //   rmdirSync(join(path, folder));
  // }
  try {
    accessSync(join(path, folder, "PERWAKILAN.pdf"));
  } catch (e) {
    console.log(folder);
    // renameSync(join(path, folder), join(path, "ALL", folder));
  }
});
