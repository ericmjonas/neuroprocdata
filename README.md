# neuroproc datasets 


This is super-preliminary and not public yet, as it's buggy! So please
be careful and tread lightly. 


Available: 
- [ ] Connectivty 
- [ ] main timeseries
- [ ] output images / frames for above timeseries
- [ ] lesion data
- [ ] memory IO 

Basic explanations of the data can be found in the ipython
notebooks included in this project. 

Notes:
- All data is stored in s3, and many of the files are massive
- All the original data was analyzed in python, and thus we have a lot
  of `.npy` files. I've made an effort to also create
  [HDF5](https://www.hdfgroup.org/HDF5/) versions that have a single
  dataset internally, `data`, which corresponds to the `.npy` file.

We have a mailing list (`neuroproc@googlegroups.com`) and
[associated Google group](https://groups.google.com/forum/#!forum/neuroproc)
for discussion. You can also create github issues if there are
problems or omissions in the data. 

### Gzipping time series

The raw timeseries are huge, ~20GB+ so I've gzipped them, which
reduces the size between 10 and 20x. There were a lot of
trade-offs: I like the `npy` format because it's easy to memory-map
in the files, etc. For reference:

```
$ time gzip pitfall-big.100000.ts.spikes.npy

real    15m53.877s
user    15m35.724s
sys     0m17.296s

```

```
$ time gunzip pitfall-big.100000.ts.spikes.npy.gz

real    4m53.549s
user    3m29.004s
sys     0m26.792s

```

