# A New Kabuverdianu-English Parallal Dataset

The two available datasets in this repository contain 2000 parallel sentences used in a machine translation experiment

This was the most time-consuming part of the experiment and, on average, it took around two to three hours to produce 100 sentences. Although the author of this paper is not a native speaker of Kabuverdianu, without their expertise in European Portuguese and previous studies of Cape Verdean Creole, adjusting and improving the quality of the noisy data from the OPUS corpus would not have been conceivable.

The filtering process was to look at the two monolingual files from the OPUS parallel dataset (http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf) line by line and check if the translation was accurate. The actual number of already parallel and usable sentences as they were was extremely low, and this number decreased as the collection grew due to the fact that the sentences, especially in some sections of the files, were repetitive.
If the sentences were completely off, we discarded them and moved to the next line.
In the case in which the target sentence was just a part of the source sentence (or the other way around), we were either deleting or adding the additional chunk so that they matched.
When sentences were slightly off by a few words, we used an online dictionary from Glosbe (https://en.glosbe.com/en) to check and modify the tokens that needed to be adjusted. This website also has a completely free-to-use machine translation interface that produces decent-quality sentences for the language pair taken into consideration in this book. To prove this, on top of the author's skills, we double-checked by taking two good parallel sentences as references and seeing if the interface was able to produce a reasonable output. Depending on the topic, the translation was either very close to the reference or the same, and this is why we started to include it in our sentence-making process in situations in which the sentence in Cape Verdean was correct, but its corresponding line in English was completely different. In such a case, we translated the sentence into English and then fed the Cape Verdean sentence to the Glosbe engine to check if our translation was correct. In case more revision was needed due to the wrong word sense, for example, we used again the dictionary. If none of these techniques were usable due to the absence of some words in the dictionary or if the sentence produced was just not satisfactory, we would discard it and move on to checking the next line.

To reach 2000 filtered and revised sentences, we went through the first 26796 sentences of the noisy corpus.

Just for my own personal satisfaction, please add a star to my project, peace.

## tokenization.py

The uploaded text files are completely untokenized. The tokenization.py file in this repository is just meant to reproduce what I have used in my experiment, but any further user should use their own if they think they can ameliorate it. 

### Reference

Jörg Tiedemann. 2012. Parallel Data, Tools and Interfaces in OPUS. In Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12), pages 2214–2218, Istanbul, Turkey. European Language Resources Association (ELRA




Contains information from NLLBv1 which is made available
under the ODC Attribution License.
