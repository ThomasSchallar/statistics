
# Number of bootstrap samples
n_bootstrap = 1000
N= len(max_obs_mag)
samplesize= int( N / 2 )

# Store bootstrap slopes
bootstrap_slopes = []

# Perform bootstrap resampling
for _ in range(n_bootstrap):
    # Resample data with replacement
    indices = random.sample(range(N), samplesize)

    resampled_mag = max_obs_mag[indices]
    resampled_log_dist = log_dist[indices]
    
    # Fit linear regression to the resampled data
    coefficients = np.polyfit(resampled_mag, resampled_log_dist, deg=1)
    slope = coefficients[0]
    
    # Store the slope
    bootstrap_slopes.append(slope)

bootstrap_slopes.sort()

# Compute the 1-sigma interval (16th and 84th percentiles)
lower_bound = np.percentile(bootstrap_slopes, 16)
upper_bound = np.percentile(bootstrap_slopes, 84)

# Print results
print(f"Bootstrap 1-sigma interval for the slope: ({lower_bound:.4f}, {upper_bound:.4f})")

alpha= 0.318
remove= int(N*alpha/2)
print(f"removing {remove} lowest and highest estimates")
cut= bootstrap_slopes[remove:-remove]
print(f"Mean slope: {np.mean(cut):.4f}")

# Plot the distribution of bootstrap slopes
plt.hist(bootstrap_slopes, bins=30, alpha=0.7, color='blue', label='Bootstrap Slopes')
plt.axvline(lower_bound, color='red', linestyle='--', label='1-sigma lower bound')
plt.axvline(upper_bound, color='green', linestyle='--', label='1-sigma upper bound')
plt.xlabel('Slope')
plt.ylabel('Frequency')
plt.title('Bootstrap Slope Distribution')
plt.legend()
plt.show()

