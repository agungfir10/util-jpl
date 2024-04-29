import { readdirSync, accessSync, renameSync, rmdirSync } from "fs";
import { unlink } from 'node:fs'
import { join } from "path";
import { naturalCompare } from "./const.js";

const path = "/Users/agungfir/Downloads/OKTOBER/KAB. SUKOHARJO";

const folders = readdirSync(path).sort(naturalCompare);

folders.forEach((folder) => {
  // const files = readdirSync(join(path, folder));
  // if (files.length === 0) {
  //   rmdirSync(join(path, folder));
  // }
  try {
    accessSync(join(path, folder, "PENGGANTI.pdf"));
  } catch (e) {
    console.log(folder);
    // renameSync(join(path, folder), join(path, "ALL", folder));
  }
  // try {
  //   accessSync(join(path, folder, "DTT.pdf"));
  // } catch (e) {
  //   console.log(folder);
  //   // renameSync(join(path, folder), join(path, "ALL", folder));
  // }
});
