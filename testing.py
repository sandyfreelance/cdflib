import pds2_cdf
import pytplot
import numpy as np

# rbsp_file = pds2_cdf.CDF("C:/temp/mavencdfs/rbsp-a-rbspice_lev-3_esrhelt_20170619_v1.1.9-00.cdf")
#  
# print(rbsp_file.attget(0,0))
#  
# print(rbsp_file.attget("UNITS",5))
#  
# print(pds2_cdf.cdfepoch.encode(rbsp_file.varget(variable='Epoch')))
# print(rbsp_file.epochrange("Epoch", starttime = pds2_cdf.cdfepoch.compute_tt2000([2017,6,19,5,5,5]), endtime = pds2_cdf.cdfepoch.compute_tt2000([2017,6,19,6,6,6])))


#lpw_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_lpw_l2_lpiv_20170725_v02_r02.cdf")
#sepanc_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_sep_l2_anc_20170725_v06_r02.cdf")
#sepl2_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_sep_l2_s1-cal-svy-full_20170725_v04_r04.cdf")
#swe_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_swe_l2_svyspec_20170725_v04_r04.cdf")
#swi_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_swi_l2_onboardsvyspec_20170725_v01_r00.cdf")


euvl3_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_euv_l3_minute_20170725_v09_r03.cdf")

print(euvl3_file.attget('var_notes', 'flag'))
bins = euvl3_file.varget('v')

time = euvl3_file.varget('x')

data = euvl3_file.varget('y')

pytplot.store_data('hello', data={'x':time, 'y':data, 'v':bins})
pytplot.options('hello', 'spec', 1)
pytplot.options('hello', 'ylog', 0)
pytplot.options('hello', 'zlog', 0)
pytplot.tplot('hello')

# euvl2_file = pds2_cdf.CDF("C:/temp/mavencdfs/mvn_euv_l2_bands_20170725_v09_r03.cdf")
# 
# data = euvl2_file.varget('data')
# time = euvl2_file.varget('time_unix')
# 
# pytplot.store_data('hello', data={'x':time, 'y':data})
# pytplot.options('hello', 'ylog', 1)
# pytplot.tplot('hello')

# tha_file= pds2_cdf.CDF("C:/temp/mavencdfs/tha_l1_fgm_20090101_v01.cdf")
# data = tha_file.varget(variable='tha_fgh', startrec=0, endrec=1000)
# time = tha_file.varget(variable='tha_fgh_time', startrec=0, endrec=1000)
# 
# pytplot.store_data('hello', data={'x':time, 'y':data})
# pytplot.tplot('hello')
#sta_file= pds2_cdf.CDF("C:/temp/mavencdfs/mvn_sta_l2_db-1024tof_20170725_v01_r05.cdf")
#print(sta_file.attget(attribute="SPACECRAFT", entry_num=0))
# times = sta_file.varget(variable='time_unix', starttime=pds2_cdf.cdfepoch.compute_tt2000([2017,7,25,5,5,5]), endtime=pds2_cdf.cdfepoch.compute_tt2000([2017,7,25,6,5,5]))
# 
# data = sta_file.varget(variable='data', starttime=pds2_cdf.cdfepoch.compute_tt2000([2017,7,25,5,5,5]), endtime=pds2_cdf.cdfepoch.compute_tt2000([2017,7,25,6,5,5]))
# 
# tof = sta_file.varget(variable='tof', starttime=pds2_cdf.cdfepoch.compute_tt2000([2017,7,25,5,5,5]), endtime=pds2_cdf.cdfepoch.compute_tt2000([2017,7,25,6,5,5]))
# 
# pytplot.store_data('hello', data={'x':times, 'y':data, 'v':tof})
# pytplot.options('hello', 'spec', 1)
# pytplot.options('hello', 'ylog', 0)
# pytplot.tplot('hello')