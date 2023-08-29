import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def plot_feature_distribution(data: pd.DataFrame, feature: dict) -> None:
    # Set style
    sns.set_style("whitegrid")

    plt.figure(figsize=(12, 6))
    if 'Story_Point' == feature['name']:
        bins = [0, 1, 2, 5, 8, 13, 21, max(data[feature['name']]) + 1]
        labels = ['1', '2', '3-5', '6-8', '9-13', '14-21', '22+']
        binned = pd.cut(data[feature['name']], bins=bins, labels=labels, right=False)
        binned_counts = binned.value_counts().sort_index()
        binned_counts.plot(kind='bar', color='blue', alpha=0.5)
        plt.ylabel('Frequency')
    else:
        sns.countplot(data=data, x=feature['name'], order=data[feature['name']].value_counts().index, palette=feature['palette'])
        plt.ylabel('Number of Issues')

    title = f"Distribution of {feature['name']}"
    plt.title(title)
    plt.xlabel(feature['label'])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(FuncFormatter(yaxis_formatter))

    save_fig(plt, title)

    plt.show()

def plot_correlation_matrix(correlation, title: str) -> None:

    plt.figure(figsize=(15, 10))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title(title)
    save_fig(plt, title)

    plt.show()

def plot_boxplot(data: pd.DataFrame, feature: str, title: str = 'Boxplot'):
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=data, x=feature)
    plt.title(title)
    plt.tight_layout()
    save_fig(plt, title)

    plt.show()

def plot_non_missing_story_points_distribution(data: pd.DataFrame):
    # Plot distribution of story points for non-missing values
    title = 'Distribution of Story Points (Non-Missing Values)'
    plt.figure(figsize=(12, 6))
    sns.histplot(data[data['Story_Point'].notna()]['Story_Point'], kde=True, bins=30, color='purple')
    plt.title(title)
    plt.xlabel('Story Points')
    plt.ylabel('Frequency')
    plt.tight_layout()

    save_fig(plt, title)

    plt.show()
def save_fig(plot, fig_name):
    PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
    fig_path = os.path.join(PROJECT_ROOT_DIR, f'reports/figures/{fig_name}.png')
    plot.savefig(fig_path, dpi=300)

def yaxis_formatter(x, _):
    return '{:,.0f}'.format(x)

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
    save_fig(plt, full_title)
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
    save_fig(plt, full_title)
    plt.show()

def plot_neural_network_training_history(history, model_name):
    title = f'Training and Validation Loss for {model_name}'
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.legend()
    plt.title()
    plt.tight_layout()
    save_fig(plt, title)
    plt.show()