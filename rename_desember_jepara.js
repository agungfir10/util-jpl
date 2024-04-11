import fs from "fs";
import path from "path";

const filepath = "D:\\DESEMBER PATI SIAP UPLOAD\\KAB. JEPARA";
const folders = fs.readdirSync(path.join(filepath));

folders.forEach((folder) => {
  const files = fs.readdirSync(path.join(filepath, folder));
  fs.renameSync(
    path.join(filepath, folder, files[0]),
    path.join(filepath, folder, `${folder}.pdf`)
  );
});
