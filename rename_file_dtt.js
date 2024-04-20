import { renameSync, accessSync, readdirSync } from "fs";
import { join } from "path";

const path = "E:\\HASIL\\T1 November\\PEKALONGAN UTARA";
const folders = readdirSync(join(path));

folders.forEach((folder) => {
  console.log(folder);
  const files = readdirSync(join(path, folder));
  files.forEach((file) => {
    if (file.includes("SPTJM")) {
      try {
        console.log(file);
        accessSync(join(path, folder, file));
        renameSync(join(path, folder, file), join(path, folder, "SPTJM.pdf"));
      } catch (e) {
        console.log(e);
      }
    }
  });
});
