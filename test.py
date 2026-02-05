{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bd8c519",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ebd0f4c0",
   "metadata": {},
   "source": [
    "# Quick example: Load CSV and plot\n",
    "This cell demonstrates reading `ride_sharing_learning_data.csv` with `pandas` and plotting `price` vs `distance` using `matplotlib`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20388703",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "Could not find 'ride_sharing_learning_data.csv' in the notebook working directory. Run the data generator first or check the file path.",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m     df = \u001b[43mpd\u001b[49m\u001b[43m.\u001b[49m\u001b[43mread_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mride_sharing_learning_data.csv\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m      7\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mFileNotFoundError\u001b[39;00m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python314\\site-packages\\pandas\\io\\parsers\\readers.py:873\u001b[39m, in \u001b[36mread_csv\u001b[39m\u001b[34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, skip_blank_lines, parse_dates, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[39m\n\u001b[32m    871\u001b[39m kwds.update(kwds_defaults)\n\u001b[32m--> \u001b[39m\u001b[32m873\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_read\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python314\\site-packages\\pandas\\io\\parsers\\readers.py:300\u001b[39m, in \u001b[36m_read\u001b[39m\u001b[34m(filepath_or_buffer, kwds)\u001b[39m\n\u001b[32m    299\u001b[39m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m300\u001b[39m parser = \u001b[43mTextFileReader\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    302\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python314\\site-packages\\pandas\\io\\parsers\\readers.py:1645\u001b[39m, in \u001b[36mTextFileReader.__init__\u001b[39m\u001b[34m(self, f, engine, **kwds)\u001b[39m\n\u001b[32m   1644\u001b[39m \u001b[38;5;28mself\u001b[39m.handles: IOHandles | \u001b[38;5;28;01mNone\u001b[39;00m = \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1645\u001b[39m \u001b[38;5;28mself\u001b[39m._engine = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_make_engine\u001b[49m\u001b[43m(\u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mengine\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python314\\site-packages\\pandas\\io\\parsers\\readers.py:1904\u001b[39m, in \u001b[36mTextFileReader._make_engine\u001b[39m\u001b[34m(self, f, engine)\u001b[39m\n\u001b[32m   1903\u001b[39m         mode += \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m-> \u001b[39m\u001b[32m1904\u001b[39m \u001b[38;5;28mself\u001b[39m.handles = \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   1905\u001b[39m \u001b[43m    \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1906\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1907\u001b[39m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mencoding\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1908\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mcompression\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1909\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmemory_map\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mmemory_map\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1910\u001b[39m \u001b[43m    \u001b[49m\u001b[43mis_text\u001b[49m\u001b[43m=\u001b[49m\u001b[43mis_text\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1911\u001b[39m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mencoding_errors\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mstrict\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1912\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mstorage_options\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1913\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   1914\u001b[39m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m.handles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python314\\site-packages\\pandas\\io\\common.py:926\u001b[39m, in \u001b[36mget_handle\u001b[39m\u001b[34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[39m\n\u001b[32m    924\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m ioargs.encoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs.mode:\n\u001b[32m    925\u001b[39m     \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m926\u001b[39m     handle = \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[32m    927\u001b[39m \u001b[43m        \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    928\u001b[39m \u001b[43m        \u001b[49m\u001b[43mioargs\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    929\u001b[39m \u001b[43m        \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[43mioargs\u001b[49m\u001b[43m.\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    930\u001b[39m \u001b[43m        \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    931\u001b[39m \u001b[43m        \u001b[49m\u001b[43mnewline\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m    932\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    933\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m    934\u001b[39m     \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'ride_sharing_learning_data.csv'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      6\u001b[39m     df = pd.read_csv(\u001b[33m'\u001b[39m\u001b[33mride_sharing_learning_data.csv\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m      7\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mFileNotFoundError\u001b[39;00m:\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mFileNotFoundError\u001b[39;00m(\u001b[33m\"\u001b[39m\u001b[33mCould not find \u001b[39m\u001b[33m'\u001b[39m\u001b[33mride_sharing_learning_data.csv\u001b[39m\u001b[33m'\u001b[39m\u001b[33m in the notebook working directory. Run the data generator first or check the file path.\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     10\u001b[39m \u001b[38;5;66;03m# Show a quick preview\u001b[39;00m\n\u001b[32m     11\u001b[39m display(df.head())\n",
      "\u001b[31mFileNotFoundError\u001b[39m: Could not find 'ride_sharing_learning_data.csv' in the notebook working directory. Run the data generator first or check the file path."
     ]
    }
   ],
   "source": [
    "# Load data and quick visual (search for CSV in workspace)\n",
    "import os, glob\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "print('notebook cwd:', os.getcwd())\n",
    "# Search recursively for the CSV in the workspace\n",
    "candidates = glob.glob('**/ride_sharing_learning_data.csv', recursive=True)\n",
    "print('found candidates:', candidates[:5])\n",
    "\n",
    "if not candidates:\n",
    "    # Fallback: explicit workspace path\n",
    "    alt = r'c:\\Users\\thomas\\ride-price-system-estimation-system\\ride_sharing_learning_data.csv'\n",
    "    if os.path.exists(alt):\n",
    "        path = alt\n",
    "    else:\n",
    "        raise FileNotFoundError(\"Could not find 'ride_sharing_learning_data.csv' in the notebook working directory or workspace. Run the data generator or check the file path.\")\n",
    "else:\n",
    "    path = candidates[0]\n",
    "\n",
    "print('loading from:', path)\n",
    "df = pd.read_csv(path)\n",
    "\n",
    "# Show a quick preview\n",
    "display(df.head())\n",
    "\n",
    "# Scatter plot: price vs distance\n",
    "plt.figure(figsize=(8,5))\n",
    "plt.scatter(df['distance'], df['price'], c='tab:blue', alpha=0.6, edgecolors='w', linewidths=0.5)\n",
    "plt.xlabel('distance')\n",
    "plt.ylabel('price')\n",
    "plt.title('Price vs Distance')\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "\n",
    "# Optional: mean price by demand (if present)\n",
    "if 'demand' in df.columns:\n",
    "    mean_by_demand = df.groupby('demand')['price'].mean().reindex(['Low','Medium','High'], fill_value=None)\n",
    "    if not mean_by_demand.dropna().empty:\n",
    "        ax = mean_by_demand.plot(kind='bar', figsize=(6,4), color=['#66c2a5','#fc8d62','#8da0cb'])\n",
    "        ax.set_ylabel('mean price')\n",
    "        ax.set_title('Mean Price by Demand')\n",
    "        plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}