{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "edhec_risk_kit.py",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1smXKO4apad_A_9_ywn9RYomOUZqkZjZ5",
      "authorship_tag": "ABX9TyMCS9Jt6lA6KLnHjgeFx/VL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lolanto-ds/portfolio_python/blob/main/edhec_risk_kit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xiq4tdwEKbuP",
        "outputId": "d5252169-bff8-4ff7-f326-b92fdff9d64f"
      },
      "source": [
        "!git clone https://github.com/lolanto-ds/portfolio_python.git"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cloning into 'portfolio_python'...\n",
            "remote: Enumerating objects: 65, done.\u001b[K\n",
            "remote: Counting objects: 100% (65/65), done.\u001b[K\n",
            "remote: Compressing objects: 100% (63/63), done.\u001b[K\n",
            "remote: Total 65 (delta 21), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (65/65), done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ChsGYRLyziIk"
      },
      "source": [
        "import pandas as pd\n"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YKGAd6ZZzRD1"
      },
      "source": [
        "def drawdown(return_series: pd.Series):\n",
        "  \"\"\"\n",
        "  Takes a time series of asset returns\n",
        "  Computes and returns a DataFrame that contains:\n",
        "  the wealth index\n",
        "  the previous peaks\n",
        "  percent drawdowns\n",
        "  \"\"\"\n",
        "  wealth_index = 1000*(1+return_series).cumprod()\n",
        "  previous_peaks = wealth_index.cummax()\n",
        "  drawdowns = (wealth_index - previous_peaks)/previous_peaks\n",
        "  return pd.DataFrame({\n",
        "      \"Wealth\": wealth_index,\n",
        "      \"Peaks\" : previous_peaks,\n",
        "      \"Drawdown\": drawdowns\n",
        "  })"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z4JGVFVBzmn7"
      },
      "source": [
        "def get_ffme_return():\n",
        "  \"\"\"\n",
        "  Load the Fama-French Dataset for the returns of the Top and Bottom Deciles by MarketCap\n",
        "  \"\"\"\n",
        "  me_m = pd.read_csv('/content/portfolio_python/data/Portfolios_Formed_on_ME_monthly_EW.csv',\n",
        "                     header=0, index_col=0, na_values=-99.99)\n",
        "  rets = me_m[['Lo 10','Hi 10']]\n",
        "  rets.columns = ['SmallCap','LargeCap']\n",
        "  rets = rets/100\n",
        "  rets.index = pd.to_datetime(rets.index, format=\"%Y%m\").to_period('M')\n",
        "  return rets\n"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 415
        },
        "id": "s_C0gGVl4COl",
        "outputId": "26992e1d-a554-4e3c-bb12-a999f3d01613"
      },
      "source": [
        "get_ffme_return()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>SmallCap</th>\n",
              "      <th>LargeCap</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1926-07</th>\n",
              "      <td>-0.0145</td>\n",
              "      <td>0.0329</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1926-08</th>\n",
              "      <td>0.0512</td>\n",
              "      <td>0.0370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1926-09</th>\n",
              "      <td>0.0093</td>\n",
              "      <td>0.0067</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1926-10</th>\n",
              "      <td>-0.0484</td>\n",
              "      <td>-0.0243</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1926-11</th>\n",
              "      <td>-0.0078</td>\n",
              "      <td>0.0270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-08</th>\n",
              "      <td>0.0241</td>\n",
              "      <td>0.0234</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-09</th>\n",
              "      <td>-0.0168</td>\n",
              "      <td>0.0087</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-10</th>\n",
              "      <td>-0.1002</td>\n",
              "      <td>-0.0657</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-11</th>\n",
              "      <td>-0.0365</td>\n",
              "      <td>0.0253</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-12</th>\n",
              "      <td>-0.1531</td>\n",
              "      <td>-0.0890</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1110 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "         SmallCap  LargeCap\n",
              "1926-07   -0.0145    0.0329\n",
              "1926-08    0.0512    0.0370\n",
              "1926-09    0.0093    0.0067\n",
              "1926-10   -0.0484   -0.0243\n",
              "1926-11   -0.0078    0.0270\n",
              "...           ...       ...\n",
              "2018-08    0.0241    0.0234\n",
              "2018-09   -0.0168    0.0087\n",
              "2018-10   -0.1002   -0.0657\n",
              "2018-11   -0.0365    0.0253\n",
              "2018-12   -0.1531   -0.0890\n",
              "\n",
              "[1110 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WvkGTe2v4cv1"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}