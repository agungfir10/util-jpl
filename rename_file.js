import { accessSync, renameSync, readdirSync, rename } from "fs";
import { join } from "path";
import { naturalCompare, splitext } from "./const.js";

const path = "F:\\FILE BARU REMBANG OKTOBER\\KAB REMBANG TAMB 3 OKT";
// const files = readdirSync(join(path)).sort(naturalCompare);
const folders = readdirSync(join(path)).sort(naturalCompare);

folders.forEach((folder) => {
  const files = readdirSync(join(path, folder)).sort(naturalCompare);
  files.forEach((file) => {
    const [filename, ext] = splitext(file);
    console.log(filename);
    renameSync(
      join(path, folder, file),
      join(path, folder, `KAB. REMBANG-${folder}-${filename}${ext}`)
    );
  });
});

// files.forEach((file) => {
//   //   const kota = file.split("-")[0];
//   //   const kec = file.split("-")[1];
//   // const desa = file.split("-")[2].split(".")[0];
//   // const kec = file.split("~")[0];
//   // const desa = file.split("~")[1].split(".")[0];
//   const [filename, ext] = splitext(file);
//   // renameSync(join(path, file), join(path, `${kota}-${kec}-${desa}.pdf`));
//   // renameSync(join(path, file), join(path, `KAB. TEGAL-${kec}-${desa}${ext}`));
//   renameSync(
//     join(path, file),
//     join(path, `KAB. BLORA-TUNJUNGAN-${filename}${ext}`)
//   );

//   // try {
//   //   // accessSync(join(path, folder, "BAST.pdf"));
//   //   const [filename, ext] = splitext(file);
//   //   console.log(ext);
//   //   // renameSync(
//   //   //   join(path, file),
//   //   //   join(path, `KOTA SEMARANG-TUGU-${filename}${ext}`)
//   //   // );
//   //   // renameSync(
//   //   //   join(path, folder, "BAST.pdf"),
//   //   //   join(path, folder, "BAST DESA.pdf")
//   //   // );
//   // } catch (e) {
//   //   console.log(file);
//   // }
//   // const files = readdirSync(join(path, folder)).sort(naturalCompare);
//   // try {
//   //   accessSync(join(path, folder, "SPTJM.pdf"));
//   // } catch (e) {
//   //   console.log(folder);
//   // }
// });
