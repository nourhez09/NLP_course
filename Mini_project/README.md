# Objective

Benchmark models to perform sentiment classification on the IMDB dataset. This project was done by HEZBRI Nour as a part 
of the validation criteria of the NLP course at ENSAE Paris.

We use part of the code in the following [repository](https://github.com/rainavyas/IMDB_Sentiment_Classification) that we would like to acknowledge.


<!-- 
# Experimental Results

| Model Architecture | Test Accuracy (%) |
| ----------------- | :-----------------: |
ELECTRA (base) encoder + classification head | 95.6 |
BERT (base-uncased) encoder + classification head | 93.8 |
RoBERTta (base) encoder + classification head | 95.4 |
XLNet (base) encoder + classification head | 95.0 |

Note that the XLNet tokenizer was adapted to force truncation to 512 tokens (to be comparable to other models) -->

### Training Details

- Initialise encoder with _model_
- Batch Size = 8
- Epochs = 2
- Learning Rate = 1e-5