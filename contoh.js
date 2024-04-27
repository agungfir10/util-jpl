import dtt from './data/SEP_REG_BATAL.json' assert {type: 'json'}
import fs from 'fs'
let newSep = [];
const reg = dtt.filter((d) => d.NO_DTT.includes('23114'))

reg.forEach(d => {
    if (d.SPTJM === undefined) {
        d.SPTJM = ''
    }

    if (d.PENGGANTI === undefined) {
        d.PENGGANTI = ''
    }

    if (d.PERWAKILAN === undefined) {
        d.PERWAKILAN = ''
    }
    newSep.push(d)
})

const newSepFilter = newSep.filter(s => !s.PERWAKILAN.includes('V'))
console.log(newSepFilter.length)
fs.writeFileSync('./data/SEP_REG_BATAL_FIX.json', JSON.stringify(newSepFilter))