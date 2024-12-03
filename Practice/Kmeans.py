 elif plot_type == "kmeans":
            # K-Means Clustering
            numeric_features = df.select_dtypes(include=['float64', 'int64']).drop(columns=['quality', 'Id'], errors='ignore') #Extracts Numeric data and remove quality and id
            scaler = StandardScaler() #Ensures all numeric features are scaled to have a mean of 0 and a standard deviation of 1.
            scaled_data = scaler.fit_transform(numeric_features)

            # Apply PCA for visualization
            pca = PCA(n_components=2) #reduce the high-dimensional data to 2 dimensions
            reduced_data = pca.fit_transform(scaled_data) # Identifies the directions (principal components) that maximize variance in the data.

            # K-Means Clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(scaled_data)

            # Create a DataFrame with PCA results and clusters
            pca_df = pd.DataFrame(reduced_data, columns=['PC1', 'PC2'])
            pca_df['Cluster'] = clusters

            # Plot the clusters
            plt.figure(figsize=(10, 10))
            sns.scatterplot(x='PC1', y='PC2', hue='Cluster', palette='tab10', data=pca_df, s=50)
            plt.title(f'K-Means Clustering with {n_clusters} Clusters (PCA)')
            plt.legend(title="Cluster")
