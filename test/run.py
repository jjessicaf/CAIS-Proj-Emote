import torch
import torch.nn as nn
from transformers import AutoTokenizer as BertTokenizer, BertModel

import pytorch_lightning as pl
import os


# class for finetuned bert classification model
class EmoteTagger(pl.LightningModule):
    def __init__(self, n_classes: int, n_training_steps=None, n_warmup_steps=None, bert_model=None):
        super().__init__()
        self.bert = bert_model
        self.classifier = nn.Linear(self.bert.config.hidden_size, n_classes)
        self.n_training_steps = n_training_steps
        self.n_warmup_steps = n_warmup_steps
        self.criterion = nn.BCELoss()

    def forward(self, input_ids, attention_mask, labels=None):
        output = self.bert(input_ids, attention_mask=attention_mask)
        output = self.classifier(output.pooler_output)
        output = torch.sigmoid(output)
        loss = 0
        if labels is not None:
            loss = self.criterion(output, labels)
        return loss, output


# runs the model on specified chat
def run():
    path = './trained_model/trained_model.pth'
    chat = "Today is a good day"

    # initialize model
    model_name = 'bert-base-cased'
    model = BertModel.from_pretrained(model_name, return_dict=True)
    tokenizer = BertTokenizer.from_pretrained(model_name)

    # use gpa if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    num_classes = 5
    label_columns = [1, 2, 3, 4, 5]

    # load the model
    test_model = EmoteTagger(
        n_classes=num_classes,
        bert_model=model
    )

    # load best weights
    src = os.path.abspath(path)
    best = torch.load(src)
    test_model.load_state_dict(best['model_state_dict'])

    # set to evaluation mode and freeze the weights
    test_model.to(device)
    test_model.eval()
    test_model.freeze()

    # dict to unconvert results
    Dict = {1: 'joebartBusiness', 2: 'joebartLongneck', 3: 'joebartWeBelieve', 4: 'LUL', 5: 'catJAM'}
    Dict = dict((k, v.lower()) for k, v in Dict.items())

    # encoder
    encoding = tokenizer.encode_plus(
        chat,
        add_special_tokens=True,
        max_length=512,
        return_token_type_ids=False,
        padding="max_length",
        return_attention_mask=True,
        return_tensors='pt',
    )

    encoding.to(device)

    _, test_prediction = test_model(encoding["input_ids"], encoding["attention_mask"])
    test_prediction = test_prediction.cpu()  # numpy doesn't work with gpu
    test_prediction = test_prediction.flatten().numpy()

    result = ["", 0]

    print("label predictions:")
    for label, prediction in zip(label_columns, test_prediction):
        print(f"{Dict[label]}: {prediction}")
        if (prediction > result[1]):
            result = [label, prediction]

    # output the result
    print('\nfinal prediction:', Dict[result[0]])


if __name__ == '__main__':
    run()


