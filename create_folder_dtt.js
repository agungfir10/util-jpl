import { mkdirSync, readdirSync } from "fs";
import { join } from "path";

const path = "E:\\DOKUMEN SEPTEMBER JATENG\\IMAGES TO DTT";

const folders = readdirSync(join(path));

folders.forEach((folder) => {
  mkdirSync(join(path, folder, "DTT"));
});
