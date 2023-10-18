import evaluate


def get_accuracy_score(predictions, actuals):
    # Calculate BLEU Score

    bleu = evaluate.load('bleu')
    rouge = evaluate.load('rouge')

    score = {}

    results = rouge.compute(predictions=predictions, references=actuals)
    bleu_results = bleu.compute(predictions=predictions, references=actuals)

    score['bleu'] = bleu_results['bleu']
    score['rouge1'] = results['rouge1']
    score['rouge2'] = results['rouge2']
    score['rougeL'] = results['rougeL']
    score['rougeLsum'] = results['rougeLsum']

    return score
