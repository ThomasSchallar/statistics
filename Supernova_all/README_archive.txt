#
# A NOTE to users of the CfA Supernova Archive
# https://lweb.cfa.harvard.edu/supernova/README_archive
#

When in doubt about a given lightcurve/spectrum, consult the original
publication (listed under "References") and/or contact its first
author.

Most of the information you will want to know about a given spectrum 
is in the header of the corresponding FITS file. Please note, however,
that not all ascii spectra have an associated FITS spectrum.

In some cases there are more spectra for a given supernova in the
archive than in the corresponding published paper. Please make sure to
always reference the paper(s) listed under "References", as these can
provide useful information on how the data was obtained/reduced etc.

   ---> PLEASE ACKNOWLEDGE USAGE OF THE CfA Supernova Archive <---

If your research benefits from the use of the CfA Supernova Archive,
we would appreciate the following acknowledgement in your paper: "This
research has made use of the CfA Supernova Archive, which is funded in
part by the National Science Foundation through grant AST 0907903."

For more information, please contact: Stéphane Blondin


***********************************
* Download information
***********************************

Lightcurves are stored in ASCII format, one file for UBVRI, another for JHK

Spectra are available for downloads as gzipped tarballs (*.tar.gz), 
one for spectra in ASCII format, another for spectra in FITS format.
The number of spectra corresponding to a given SN is given in square
brackets, and corresponds to the number of ASCII spectra for that SN.

Executing the following command will unpack the entire archive in your current directory:

   gunzip < filename.tar.gz | tar xvf -

For bulk downloads on the other hand, executing the above command will create 
the following directories in your current directory:

cfaspec_M08snIa.tar.gz	One directory per SN name (snYYYYxx/)
cfalc_allsn/		all CfA SN lightcurves
cfalc_allsnIa/		all CfA SN Ia lightcurves
cfalc_J06snIa/		all CfA SN Ia lightcurves from Jha et al. 2006, AJ 131, 527
cfalc_R99snIa/		all CfA SN Ia lightcurves from Riess et al. 1999, AJ 117, 707


***********************************
* Supernova types
***********************************

Ia-norm    : spectroscopically/photometrically "normal" type-Ia supernovae
Ia-91t     : type-Ia supernovae whose lightcurves/spectra resemble those of SN 1991T
Ia-91bg    : type-Ia supernovae whose lightcurves/spectra resemble those of SN 1991bg
Ia-pec     : all other type-Ia supernovae (e.g., 2000cx)

Ib-norm    : "normal" type-Ib supernovae
Ib-pec     : "peculiar" type-Ib supernovae

Ic-norm    : "normal" type-Ic supernovae
Ic-pec     : "peculiar" type-Ic supernovae
Ic-hyper   : type-Ic supernovae with unusually broad spectroscopic features, sometimes associated with GRBs

II-norm    : "normal" type-II supernovae
II-pec     : "peculiar" type-II supernovae (e.g., 1987A!)
IIL        : type-II "linear" supernovae
IIn        : type-II "narrow" supernovae
IIP        : type-II "plateau" supernovae

IIb        : type-IIb supernovae (transition II -> Ib, e.g., 1993J) 



***********************************
* Lightcurves
***********************************

   Usually one file for optical (UBVRrIi) data, another for infrared (JHK) data.
   Dates sometimes appear as MJD, JD-2400000, JD-2450000 (check file header!)
   For each band, we give the apparent magnitude in that band and the 1 sigma error.
   Magnitudes/errors are given as "99.99/9.99" when data is lacking on a given date.

   --->   Look at file header for more information   <---

#-------------------------------------------------------------------
README file for lightcurves from Jha et al. 2006, AJ 131, 527

UBVRI photometry of 44 SN Ia
Jha et al. 2006, AJ 131, 527

All objects except for SN 2000cx were reduced with PSF-matched galaxy
template subtraction (*.snphot.dat). SN 2000cx was reduced with
PSF-fitting photometry (sn00cx.ubvri.psfphot.dat). See text for
details and references.

Each file contains 11 columns: heliocentric Julian date, U magnitude,
U magnitude uncertainty, B mag, B mag uncertainty, V mag, V mag
uncertainty, R mag, R mag uncertainty, I mag, and I mag
uncertainty. Entries without data are tabulated as mag = 99.999,
uncertainty = 9.999.

Please direct questions or comments to saurabh @ slac.stanford.edu
#-------------------------------------------------------------------



***********************************
* Spectra
***********************************

File naming convention:

   snYYYYxx-YYYYMMDD(-[01-99])(-telescope)(-grating)(-z)(-dered)(-variance).{fits,flm,fnu}

   snYYYYxx      : supernova name (e.g., sn2006aj)
   -YYYYMMDD     : UT date of observation (e.g., 20060222 for 22 Feb 2006)
   -[01-99]      : for multiple exposures on a same UT date, -01 indicates the 1st exposure, -02 the 2nd etc.

   -telescope    : name of telescope or instrument; choices are:
			-fast	FAST spectrograph onboard the 1.5m telescope at FLWO, Mt. Hopkins, AZ
			-hale	Palomar observatory 200" Hale Telescope
			-mmt	MMT 6.5m telescope at FLWO, Mt. Hopkins, AZ
			-iue	International Ultraviolet Explorer satellite
			-hst	Hubble Space Telescope
			-wht	William Herschel Telescope (4.2m) at ING, La Palma, Spain
			-mdm    MDM observatory, Kitt Peak 

   -grating	 : grating/grism information
	-blue<NUM> : spectrum taken with a "blue" grating; sometimes the NUM of grating lines is specified (e.g., blue600)
   	-std<NUM>  : spectrum taken with a "standard" grating; sometimes the NUM of grating lines is specified
   	-red<NUM>  : spectrum taken with a "red" grating; sometimes the NUM of grating lines is specified
   	-bsr	   : combined "blue", "std", and/or "red" spectrum
   	-g<NUM>    : spectrum taken with a grating of NUM lines (e.g., -g300)

   -z            : indicates the spectrum has been deredshifted
   -dered        : indicates the spectrum has been dereddened
   -variance     : indicates this is the corresponding variance spectrum

   .fits         : indicates the file is in FITS format
   .flm          : indicates this ASCII spectrum is in units of F_lambda (usually 1e-15 erg/s/cm^2/A)
   .fnu          : indicates this ASCII spectrum is in units of F_nu

NOTES:
(1) Wavelength has units of Angstroems 
(2) When there are multiple exposures on the same UT date, the FITS
    spectra are combined into a *single* ASCII spectrum
