import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def plot_feature_distribution(data: pd.DataFrame, feature: dict, palette: str = 'deep'):
    # Set style
    sns.set_style("whitegrid")

    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x=feature['name'], order=data[feature['name']].value_counts().index, palette=palette)
    plt.title(f"Distribution of {feature['name']}")
    plt.ylabel('Number of Issues')
    plt.xlabel(feature['label'])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(FuncFormatter(yaxis_formatter))

    plt.show()

def plot_feature_binned_distribution(data: pd.DataFrame, feature: dict, palette: str = 'deep'):
    sns.set_style("whitegrid")

    plt.figure(figsize=(12, 6))
    bins = [0, 1, 2, 5, 8, 13, 21, max(data[feature['name']]) + 1]
    labels = ['1', '2', '3-5', '6-8', '9-13', '14-21', '22+']
    binned = pd.cut(data[feature['name']], bins=bins, labels=labels, right=False)
    binned_counts = binned.value_counts().sort_index()
    binned_counts.plot(kind='bar', color='blue', alpha=0.5)
    plt.title(f"Distribution of {feature['name']}")
    plt.xlabel(f"{feature['name']} Ranges")
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(FuncFormatter(yaxis_formatter))

    plt.show()

def plot_categorical_distribution(df, feature_name):
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x=feature_name, order=df[feature_name].value_counts().index)
    plt.title(f'Distribution of {feature_name}')
    plt.xticks(rotation=45)
    plt.show()

def plot_scatter(df, x_feature, y_feature):
    plt.figure(figsize=(10,5))
    sns.scatterplot(data=df, x=x_feature, y=y_feature)
    plt.title(f'{x_feature} vs {y_feature}')
    plt.show()

def plot_correlation_matrix(df):
    correlation_matrix = df.corr()
    plt.figure(figsize=(15,10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplot(data: pd.DataFrame, feature: str, title: str = 'Boxplot'):
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=data, x=feature)
    plt.title(title)
    plt.tight_layout()

    plt.show()

def plot_boxplot_for_outliers(data: pd.DataFrame, columns: list, title: str, remove_empty_subplots: bool = False):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
    fig.suptitle(title, fontsize=16)

    for i, col in enumerate(columns):
        sns.boxplot(x=data[col], ax=axes[i // 2, i % 2], color='teal')
        axes[i // 2, i % 2].set_title(col)
        axes[i // 2, i % 2].set_xlabel('')

    # Remove empty subplot
    if remove_empty_subplots:
        fig.delaxes(axes[1, 1])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
def plot_non_missing_story_points_distribution(data: pd.DataFrame):
    # Plot distribution of story points for non-missing values
    plt.figure(figsize=(12, 6))
    sns.histplot(data[data['Story_Point'].notna()]['Story_Point'], kde=True, bins=30, color='purple')
    plt.title('Distribution of Story Points (Non-Missing Values)')
    plt.xlabel('Story Points')
    plt.ylabel('Frequency')
    plt.tight_layout()

    plt.show()
def save_fig(fig, fig_name):
    plt.savefig(fig_name, bbox_inches='tight')
    plt.close()

def yaxis_formatter(x, _):
    return '{:,.0f}'.format(x)

def plot_actual_vs_predictedx(y_test, y_pred):
    # Scatter plot of Actual vs. Predicted values
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.scatterplot(y_test, y_pred, alpha=0.5)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', lw=2, color='red')
    plt.xlabel('Actual Story Points')
    plt.ylabel('Predicted Story Points')
    plt.title('Actual vs. Predicted Story Points')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_residualx(y_test, y_pred):
    # Residual Plot
    plt.subplot(1, 2, 2)
    residuals = y_test - y_pred
    sns.scatterplot(y_test, residuals, alpha=0.5)
    plt.axhline(0, linestyle='--', lw=2, color='red')
    plt.xlabel('Actual Story Points')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_actual_vs_predicted(y_test, y_pred, model_name='', title='Actual vs. Predicted', xlabel='Actual Values', ylabel='Predicted Values'):
    # If model_name is provided, append it to the title
    full_title = f"{title} for {model_name}" if model_name else title

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # Diagonal line
    plt.title(full_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_residual(y_test, y_pred, model_name='', title='Residual Plot', xlabel='Predicted Values', ylabel='Residuals'):
    # Calculate residuals
    residuals = y_test - y_pred

    # If model_name is provided, append it to the title
    full_title = f"{title} for {model_name}" if model_name else title

    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='red', linestyle='--')  # Horizontal line at y=0 for reference
    plt.title(full_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_neural_network_training_history(history, model_name):
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.legend()
    plt.title(f'Training and Validation Loss for {model_name}')
    plt.show()