import cities from './data/DATA_WILAYAH_PENERIMA_TAMBAHAN_2.json' assert {type: 'json'}
import { accessSync } from 'fs'
import { join } from 'path'

const path = '/Users/agungfir/Downloads/KAB. REMBANG TAMBAHAN 3 SEPTEMBER'

cities.forEach(city => {
    const { KOTA, KECAMATAN, DESA } = city;
    if (KOTA === 'KAB. REMBANG') {
        try {
            accessSync(join(path, `${KOTA}-${KECAMATAN}-${DESA}`))
        } catch (e) {
            console.log(`${KOTA}-${KECAMATAN}-${DESA}`)
        }
    }
})