# genetic-unconcatenator
Transform a sequence of spaceless letters into the most probable collection of words

Run
---
`$ python genetic-split.py
rosesareredvioletsarebluesugarissweetandsoareyou
1: rose sar er ed v iol ets are b lu e s ugarissw e eta nds o a re you - 37 errors (0)
2: ro ses are r e d vio let s a re b lue s ug a r i s sweeta nd so are y o u - 35 errors (0)
3: rose s a re re dviol et sa re blue sugar is s w e e ta nd so a r e yo u - 29 errors (0)
4: rose s a re re dviol et sa re blue sugar issw ee t and so are y o u - 26 errors (0)
5: ro se s a re re dviol et sa re blue sugar issw ee t and so are y o u - 30 errors (0)
6: ros e sa re r e dviol et sa re blue sugar issw ee t and so are y o u - 31 errors (0)
7: r o s es are red vi o l et s are blue s u gar is s w e e ta nd so a r eyo u - 30 errors (0)

...
...

108: roses are red violets a re blue sugar is sweet and so are you - 2 errors (7)
109: roses are red violets a re blue sugar is sweet and so are you - 2 errors (8)
110: roses are red violets a re blue sugar is sweet and so are you - 2 errors (9)
111: roses are red violets are blue sugar is sweet and so are you - 0 errors (10)

Best individual - 00001001001000000100100010000101000010010100100
`