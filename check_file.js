import { readdirSync, accessSync, renameSync } from "fs";
import { join } from "path";
import { naturalCompare } from "./const.js";

const path = "E:\\DOKUMEN NOVEMBER REGULER JATENG\\KAB. TEGAL";

const folders = readdirSync(path).sort(naturalCompare);

folders.forEach((folder) => {
  try {
    accessSync(join(path, folder, "PERWAKILAN.pdf"));
  } catch (e) {
    console.log(folder);
    // renameSync(join(path, folder), join(path, "ALL", folder));
  }
});
