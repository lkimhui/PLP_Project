import evaluate
import matplotlib.pyplot as plt


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


'''
Function to plot scores
'''

def plot_score(before_fine_tuning, after_fine_tuning):
    # Sample Data :
    # after_fine_tuning ={'bleu': 0.4758615039897668, 'rouge1': 0.7425759708838753, 'rouge2': 0.6156175488991765, 'rougeL': 0.6427824121095069, 'rougeLsum': 0.6438283149241684}
    # before_fine_tuning ={'bleu': 0.06178770620151817, 'rouge1': 0.2777032803391897, 'rouge2': 0.12812388655907128, 'rougeL': 0.19021536111533438, 'rougeLsum': 0.1902335731113}

    # Metrics and their corresponding scores
    metrics = list(before_fine_tuning.keys())
    before_scores = list(before_fine_tuning.values())
    after_scores = list(after_fine_tuning.values())

    # Create a bar chart
    fig, ax = plt.subplots()
    width = 0.35
    x = range(len(metrics))

    ax.bar(x, before_scores, width, label='Before Fine-Tuning')
    ax.bar([i + width for i in x], after_scores, width, label='After Fine-Tuning')

    ax.set_xlabel('Metrics')
    ax.set_ylabel('Scores')
    ax.set_title('Scores Before and After Fine-Tuning T5 Model')
    ax.set_xticks([i + width / 2 for i in x])
    ax.set_xticklabels(metrics)
    ax.legend()

    plt.show()
