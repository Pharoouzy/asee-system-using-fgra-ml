import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_distribution(df, feature_name):
    plt.figure(figsize=(10,5))
    sns.distplot(df[feature_name], kde=True, bins=30)
    plt.title(f'Distribution of {feature_name}')
    plt.show()

def plot_categorical_distribution(df, feature_name):
    plt.figure(figsize=(10,5))
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

def plot_boxplot(df, feature_name):
    plt.figure(figsize=(10,5))
    sns.boxplot(data=df, x=feature_name)
    plt.title(f'Boxplot of {feature_name}')
    plt.show()