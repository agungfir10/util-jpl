import cities from "./data/DES_REG_UPLOAD.json" assert { type: "json" };
import { accessSync } from "fs";
import { join } from "path";

const path = "E:\\DOKUMEN DESEMBER JATENG\\KOTA PEKALONGAN";

cities.forEach((city) => {
  const { KOTA, KECAMATAN, DESA } = city;
  if (KOTA === "KOTA PEKALONGAN") {
    try {
      accessSync(join(path, `${KOTA}-${KECAMATAN}-${DESA}`));
    } catch (e) {
      console.log(`${KOTA}-${KECAMATAN}-${DESA}`);
    }
  }
});
