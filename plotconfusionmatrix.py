from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

actual = ['m', 'nm', 'm', 'm', 'm', 'nm', 'nm', 'm', 'm', 'nm', 'nm', 'm', 'nm', 'm', 'nm', 'nm', 'nm', 'm', 'm', 'nm']
predicted = ['m', 'nm', 'm', 'm', 'm', 'nm', 'nm', 'm', 'm', 'nm', 'nm', 'm', 'nm', 'm', 'nm', 'nm', 'm', 'm', 'm', 'nm']
labels = ['m', 'nm']
cm = confusion_matrix(actual, predicted, labels)
# print(cm)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(cm)
# plt.title('Confusion matrix of the classifier')
# fig.colorbar(cax)
# ax.set_xticklabels([''] + labels)
# ax.set_yticklabels([''] + labels)
# plt.xlabel('Predicted')
# plt.ylabel('True')
# plt.show()

ax = plt.subplot()
sns.heatmap(cm, annot=True, ax=ax) #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(['Cancerous \n (65% THP)', 'Non-cancerous \n (65% PHA)'])
ax.yaxis.set_ticklabels(['Non-cancerous \n (65% PHA) ', 'Cancerous \n (65% THP)'])
plt.savefig('confusion_matrix.png')
plt.show()