# Mooncake

This project aims to classify, based on natural language processing, the curriculum vitae from candidates for job vacancies. This project was, initially, built to the project management II discipline, nonetheless, ended in some kind of commercial product for HR consulting companies. This project is optimised for python 3.6.

-------------------------

## Project Structure - Directories ##

* __Data:__ _datasets_ directory;
* __Drivers:__ webdrivers and webcrawlers;
* __Scripts:__ _python_ scripts directory.

-------------------------

## Modules ##

- __scraper:__ The webscraping module (module responsible for extracting the CVs from web);
- __pdf_converter:__ The pdf-to-image module (due the OCR incapability to extract from pdf extensions, it is necessary to convert them into image files).
- __ocr:__ The image-to-text module (an machine learning model for image-to-text extraction);
- __classifier:__ The test classifier module (just an experimental module) _to be substituted in future_;
- __val_alg:__ The machine learning's fitting module _to be implemented in future_;
- __main:__ The machine learning's classifiers module _to be implemented in future_.

_obs: due the low number of CVs. The presentation to investidors was maded using dividends receipts from Argentina Stock Exchange (Bolsar)._

-------------------------

## Requirements ##

This project, as dependencies, require the following python libraries:

- scikit-learn;
- pandas;

To install them, in your anaconda envoironment or virtual envoironment, run the following command:

      pip install sklearn pandas

-------------------------

## Results ##

#### Models Accuracy
1. The Random Forest model assertiveness rate was: 83.33 %.
2. The dumb algorithm assertiveness rate was 50.00 %. - _independent of attributes, the model always infers Finalised.

#### Confusion Matrix
|                | Finalised | Not Finalised|
|----------------|-----------|--------------|
| Finalised      |        5  |            0 |
| Not Finalised  |        1  |            0 |

-------------------------
