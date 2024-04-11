import { mkdirSync, readdirSync } from "fs";
import { join } from "path";

const path = "E:\\DOKUMEN SEPTEMBER JATENG\\IMAGES TO PENGGANTI";

const folders = readdirSync(join(path));

folders.forEach((folder) => {
  mkdirSync(join(path, folder, "PENGGANTI"));
});
