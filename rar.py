#! /usr/bin/python

import enquiries
from zipfile import ZipFile
import patoolib

print ( '' )
print ( "█▄▄▄▄ ██   █▄▄▄▄       █ ▄▄ ▀▄    ▄ " )
print ( "█  ▄▀ █ █  █  ▄▀       █   █  █  █  " )
print ( "█▀▀▌  █▄▄█ █▀▀▌        █▀▀▀    ▀█   " )
print ( '█  █  █  █ █  █        █       █    ' )
print ( '  █      █   █       ██ █    ▄▀     ' )
print ( " ▀      █   ▀            ▀          " )
print ( "       ▀                            " )
print ( '' )

mopt = ['Zip' , 'RaR' , 'Exit']
mcoi = enquiries.choose ( 'Choose archive extension: ' , mopt )

if mcoi == ('RaR') :
    ropt = ['Extract' , 'Exit']
    rcoi = enquiries.choose ( 'Choose one of the options below: ' , ropt )

    if rcoi == ('Extract') :
        rarnamesnaf = input ( 'Enter file name without (.RAR) extension -->' )
        rarpathsnaf = input ( 'Enter extraction path for the previously selected archive -->' )
        patoolib.extract_archive ( f"{rarnamesnaf}.rar" , outdir=f"{rarpathsnaf}" )
        print ( 'Done extracting... Exiting.' )

    if rcoi == ('Exit') :
        print ( 'Exiting...' )
        exit ( )

if mcoi == ('Zip') :
    zzopt = ['Extract' , 'Exit']
    zzcoi = enquiries.choose ( 'Choose one of the options below: ' , zzopt )

if zzcoi == ('Extract') :
    zopt = ['Extract created folder with the same name as file' , 'Extract in custom named folder' , 'Exit']
    zcoi = enquiries.choose ( 'Choose one of the options below: ' , zopt )

    if zcoi == ('Extract created folder with the same name as file') :
        ECFFileName = input ( 'Input file name without .zip extensions -->' )
        # FoldName = input('Input folder name to create -->')
        with ZipFile ( f"{ECFFileName}.zip" , 'r' ) as zipObj :
            zipObj.extractall ( f'{ECFFileName}' )
            print ( 'Done extracting into created folder! Exiting!' )

    if zcoi == ('Extract in custom named folder') :
        ECFFileName = input ( 'Input file name without .zip extensions -->' )
        FoldName = input ( 'Input folder name to create -->' )
        with ZipFile ( f"{ECFFileName}.zip" , 'r' ) as zipObj :
            zipObj.extractall ( f'{FoldName}' )
            print ( 'Done extracting into created folder! Exiting!' )

if zcoi == ('Exit') :
    print ( 'Exiting' )
    exit ( )

if zcoi == ('Extract in this folder') :
    EFFileName = input ( 'Input file name -->' )
    with ZipFile ( EFFileName , 'r' ) as zipObj :
        zipObj.extractall ( 'zipper-temp' )
        print ( 'Done extracting! Exiting!' )

if zzcoi == ('Exit') :
    print ( 'Exiting' )
    exit ( )

    if mcoi == ('Exit') :
        print ( 'Exiting' )
        exit ( )
