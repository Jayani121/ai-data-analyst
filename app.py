import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f7f9fc;
    }

    /* Main title */
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    /* KPI cards */
    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        min-height: 120px;
    }

    .kpi-title {
        font-size: 14px;
        color: #6b7280;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: 700;
    }

    /* Section headers */
    .section-title {
        font-size: 23px;
        font-weight: 650;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* Insight box */
    .insight-box {
        background-color: white;
        padding: 16px;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        margin-bottom: 10px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("📊 AI Data Analyst")

    st.caption(
        "Interactive data analysis "
        "and business insights"
    )

    st.divider()

    st.write("### 📌 Dashboard")

    st.write(
        "Upload a CSV file to explore "
        "your data."
    )

    st.divider()

    st.write("### 🚀 Features")

    st.write("📋 Data Preview")
    st.write("📊 Dataset Analysis")
    st.write("🎛️ Interactive Filters")
    st.write("📈 Visual Analytics")
    st.write("💡 Business Insights")
    st.write("💬 Data Q&A")
    st.write("📥 Data Download")

    st.divider()

    st.caption(
        "Built with Python & Streamlit"
    )

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">📊 AI Data Analyst</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Upload your dataset and turn raw data into '
    'clear business insights.'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# FILE UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📁 Upload your CSV file",
    type=["csv"]
)

# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    # -----------------------------------------------------
    # READ DATA
    # -----------------------------------------------------

    df = pd.read_csv(uploaded_file)

    st.success(
        "Dataset uploaded successfully! 🎉"
    )

    # -----------------------------------------------------
    # DATASET OVERVIEW
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '📋 Dataset Overview'
        '</div>',
        unsafe_allow_html=True
    )

    overview1, overview2, overview3 = st.columns(3)

    with overview1:

        st.metric(
            "Rows",
            f"{df.shape[0]:,}"
        )

    with overview2:

        st.metric(
            "Columns",
            f"{df.shape[1]:,}"
        )

    with overview3:

        st.metric(
            "Missing Values",
            f"{int(df.isnull().sum().sum()):,}"
        )

    # -----------------------------------------------------
    # DATA PREVIEW
    # -----------------------------------------------------

    with st.expander(
        "📋 View Dataset Preview",
        expanded=True
    ):

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    # -----------------------------------------------------
    # SUMMARY STATISTICS
    # -----------------------------------------------------

    with st.expander(
        "📈 View Summary Statistics"
    ):

        st.dataframe(
            df.describe(
                include="all"
            ).transpose(),
            use_container_width=True
        )

    # -----------------------------------------------------
    # MISSING VALUES
    # -----------------------------------------------------

    with st.expander(
        "🔍 Missing Value Analysis"
    ):

        missing_values = df.isnull().sum()

        missing_df = pd.DataFrame(
            {
                "Column": missing_values.index,
                "Missing Values":
                    missing_values.values
            }
        )

        st.dataframe(
            missing_df,
            use_container_width=True
        )

    # =====================================================
    # DASHBOARD
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '📊 Interactive Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    dashboard_df = df.copy()

    # =====================================================
    # FILTERS
    # =====================================================

    st.write("### 🎛️ Filters")

    filter1, filter2, filter3 = st.columns(3)

    # -----------------------------------------------------
    # REGION
    # -----------------------------------------------------

    with filter1:

        if "Region" in dashboard_df.columns:

            regions = (
                dashboard_df["Region"]
                .dropna()
                .unique()
                .tolist()
            )

            selected_regions = st.multiselect(
                "🌍 Region",
                regions,
                default=regions
            )

            dashboard_df = dashboard_df[
                dashboard_df["Region"].isin(
                    selected_regions
                )
            ]

    # -----------------------------------------------------
    # CATEGORY
    # -----------------------------------------------------

    with filter2:

        if "Category" in dashboard_df.columns:

            categories = (
                dashboard_df["Category"]
                .dropna()
                .unique()
                .tolist()
            )

            selected_categories = st.multiselect(
                "🛍️ Category",
                categories,
                default=categories
            )

            dashboard_df = dashboard_df[
                dashboard_df["Category"].isin(
                    selected_categories
                )
            ]

    # -----------------------------------------------------
    # DATE
    # -----------------------------------------------------

    with filter3:

        if "Date" in dashboard_df.columns:

            dashboard_df["Date"] = pd.to_datetime(
                dashboard_df["Date"],
                errors="coerce"
            )

            valid_dates = (
                dashboard_df["Date"]
                .dropna()
            )

            if not valid_dates.empty:

                min_date = (
                    valid_dates.min().date()
                )

                max_date = (
                    valid_dates.max().date()
                )

                selected_dates = st.date_input(
                    "📅 Date Range",
                    value=(
                        min_date,
                        max_date
                    ),
                    min_value=min_date,
                    max_value=max_date
                )

                if len(selected_dates) == 2:

                    start_date = pd.Timestamp(
                        selected_dates[0]
                    )

                    end_date = (
                        pd.Timestamp(
                            selected_dates[1]
                        )
                        + pd.Timedelta(days=1)
                        - pd.Timedelta(seconds=1)
                    )

                    dashboard_df = dashboard_df[
                        (
                            dashboard_df["Date"]
                            >= start_date
                        )
                        &
                        (
                            dashboard_df["Date"]
                            <= end_date
                        )
                    ]

    # =====================================================
    # KPI SECTION
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '📌 Key Performance Indicators'
        '</div>',
        unsafe_allow_html=True
    )

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    # -----------------------------------------------------
    # TOTAL SALES
    # -----------------------------------------------------

    with kpi1:

        if "Sales" in dashboard_df.columns:

            total_sales = (
                dashboard_df["Sales"].sum()
            )

            st.metric(
                "💰 Total Sales",
                f"{total_sales:,.0f}"
            )

        else:

            st.metric(
                "💰 Total Sales",
                "N/A"
            )

    # -----------------------------------------------------
    # AVERAGE SALES
    # -----------------------------------------------------

    with kpi2:

        if "Sales" in dashboard_df.columns:

            average_sales = (
                dashboard_df["Sales"].mean()
            )

            st.metric(
                "📈 Avg. Sales",
                f"{average_sales:,.0f}"
            )

        else:

            st.metric(
                "📈 Avg. Sales",
                "N/A"
            )

    # -----------------------------------------------------
    # TOTAL QUANTITY
    # -----------------------------------------------------

    with kpi3:

        if "Quantity" in dashboard_df.columns:

            total_quantity = (
                dashboard_df["Quantity"].sum()
            )

            st.metric(
                "📦 Quantity",
                f"{total_quantity:,.0f}"
            )

        else:

            st.metric(
                "📦 Quantity",
                "N/A"
            )

    # -----------------------------------------------------
    # FILTERED RECORDS
    # -----------------------------------------------------

    with kpi4:

        st.metric(
            "📋 Records",
            f"{len(dashboard_df):,}"
        )

    # =====================================================
    # CHARTS
    # =====================================================

    chart_col1, chart_col2 = st.columns(2)

    # -----------------------------------------------------
    # PRODUCT SALES
    # -----------------------------------------------------

    with chart_col1:

        if (
            "Product" in dashboard_df.columns
            and "Sales" in dashboard_df.columns
        ):

            st.write("### 🏆 Sales by Product")

            product_sales = (
                dashboard_df
                .groupby("Product")["Sales"]
                .sum()
                .sort_values(
                    ascending=False
                )
            )

            st.bar_chart(
                product_sales
            )

    # -----------------------------------------------------
    # REGION SALES
    # -----------------------------------------------------

    with chart_col2:

        if (
            "Region" in dashboard_df.columns
            and "Sales" in dashboard_df.columns
        ):

            st.write("### 🌍 Sales by Region")

            region_sales = (
                dashboard_df
                .groupby("Region")["Sales"]
                .sum()
                .sort_values(
                    ascending=False
                )
            )

            st.bar_chart(
                region_sales
            )

    # -----------------------------------------------------
    # CATEGORY SALES
    # -----------------------------------------------------

    if (
        "Category" in dashboard_df.columns
        and "Sales" in dashboard_df.columns
    ):

        st.write("### 🛍️ Sales by Category")

        category_sales = (
            dashboard_df
            .groupby("Category")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        st.bar_chart(
            category_sales
        )

    # -----------------------------------------------------
    # SALES TREND
    # -----------------------------------------------------

    if (
        "Date" in dashboard_df.columns
        and "Sales" in dashboard_df.columns
    ):

        st.write("### 📈 Sales Trend")

        trend_df = (
            dashboard_df
            .groupby("Date")["Sales"]
            .sum()
            .sort_index()
        )

        st.line_chart(
            trend_df
        )

    # =====================================================
    # AUTOMATIC BUSINESS INSIGHTS
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '💡 Automatic Business Insights'
        '</div>',
        unsafe_allow_html=True
    )

    insights = []

    # -----------------------------------------------------
    # TOTAL SALES
    # -----------------------------------------------------

    if "Sales" in dashboard_df.columns:

        total_sales = (
            dashboard_df["Sales"].sum()
        )

        insights.append(
            f"💰 Total sales generated: "
            f"**{total_sales:,.2f}**."
        )

    # -----------------------------------------------------
    # TOP PRODUCT
    # -----------------------------------------------------

    if (
        "Product" in dashboard_df.columns
        and "Sales" in dashboard_df.columns
    ):

        product_sales = (
            dashboard_df
            .groupby("Product")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        if not product_sales.empty:

            top_product = (
                product_sales.index[0]
            )

            top_value = (
                product_sales.iloc[0]
            )

            insights.append(
                f"🏆 **{top_product}** is the "
                f"top-selling product with "
                f"sales of **{top_value:,.2f}**."
            )

    # -----------------------------------------------------
    # BEST REGION
    # -----------------------------------------------------

    if (
        "Region" in dashboard_df.columns
        and "Sales" in dashboard_df.columns
    ):

        region_sales = (
            dashboard_df
            .groupby("Region")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        if not region_sales.empty:

            top_region = (
                region_sales.index[0]
            )

            top_value = (
                region_sales.iloc[0]
            )

            insights.append(
                f"🌍 **{top_region}** is the "
                f"best-performing region with "
                f"sales of **{top_value:,.2f}**."
            )

    # -----------------------------------------------------
    # BEST CATEGORY
    # -----------------------------------------------------

    if (
        "Category" in dashboard_df.columns
        and "Sales" in dashboard_df.columns
    ):

        category_sales = (
            dashboard_df
            .groupby("Category")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        if not category_sales.empty:

            top_category = (
                category_sales.index[0]
            )

            top_value = (
                category_sales.iloc[0]
            )

            insights.append(
                f"🛍️ **{top_category}** is the "
                f"highest-performing category with "
                f"sales of **{top_value:,.2f}**."
            )

    # -----------------------------------------------------
    # TOTAL QUANTITY
    # -----------------------------------------------------

    if "Quantity" in dashboard_df.columns:

        total_quantity = (
            dashboard_df["Quantity"].sum()
        )

        insights.append(
            f"📦 Total quantity sold: "
            f"**{total_quantity:,.0f}** units."
        )

    # -----------------------------------------------------
    # BEST SALES DATE
    # -----------------------------------------------------

    if (
        "Date" in dashboard_df.columns
        and "Sales" in dashboard_df.columns
    ):

        daily_sales = (
            dashboard_df
            .groupby("Date")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        if not daily_sales.empty:

            best_date = (
                daily_sales.index[0]
            )

            best_value = (
                daily_sales.iloc[0]
            )

            formatted_date = pd.Timestamp(
                best_date
            ).strftime("%Y-%m-%d")

            insights.append(
                f"📅 Highest sales were recorded "
                f"on **{formatted_date}**, with "
                f"sales of **{best_value:,.2f}**."
            )

    # -----------------------------------------------------
    # DISPLAY INSIGHTS
    # -----------------------------------------------------

    if insights:

        for insight in insights:

            st.info(insight)

    else:

        st.warning(
            "Not enough compatible columns "
            "to generate business insights."
        )

    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '📥 Download Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    csv_data = (
        dashboard_df
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="📥 Download Filtered Data",
        data=csv_data,
        file_name="filtered_analysis.csv",
        mime="text/csv"
    )

    # =====================================================
    # SMART Q&A
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '💬 Ask Questions About Your Data'
        '</div>',
        unsafe_allow_html=True
    )

    question = st.text_input(
        "Ask a question:",
        placeholder=(
            "Example: What is the total sales?"
        )
    )

    if st.button(
        "🔎 Analyze Question"
    ) and question:

        q = question.lower()

        # -------------------------------------------------
        # TOTAL SALES
        # -------------------------------------------------

        if (
            "total sales" in q
            or "sum of sales" in q
        ):

            if "Sales" in dashboard_df.columns:

                total_sales = (
                    dashboard_df["Sales"]
                    .sum()
                )

                st.success(
                    f"💰 Total Sales: "
                    f"{total_sales:,.2f}"
                )

            else:

                st.warning(
                    "Sales column not found."
                )

        # -------------------------------------------------
        # AVERAGE SALES
        # -------------------------------------------------

        elif (
            "average sales" in q
            or "mean sales" in q
        ):

            if "Sales" in dashboard_df.columns:

                average_sales = (
                    dashboard_df["Sales"]
                    .mean()
                )

                st.success(
                    f"📊 Average Sales: "
                    f"{average_sales:,.2f}"
                )

            else:

                st.warning(
                    "Sales column not found."
                )

        # -------------------------------------------------
        # TOP PRODUCT
        # -------------------------------------------------

        elif (
            "highest sales" in q
            or "best selling product" in q
            or "top product" in q
        ):

            if (
                "Product" in dashboard_df.columns
                and "Sales" in dashboard_df.columns
            ):

                product_sales = (
                    dashboard_df
                    .groupby("Product")["Sales"]
                    .sum()
                    .sort_values(
                        ascending=False
                    )
                )

                if not product_sales.empty:

                    top_product = (
                        product_sales.index[0]
                    )

                    top_value = (
                        product_sales.iloc[0]
                    )

                    st.success(
                        f"🏆 Top Product: "
                        f"{top_product}"
                    )

                    st.write(
                        f"Total Sales: "
                        f"**{top_value:,.2f}**"
                    )

            else:

                st.warning(
                    "Product or Sales column "
                    "not found."
                )

        # -------------------------------------------------
        # TOP REGION
        # -------------------------------------------------

        elif (
            "highest sales region" in q
            or "best region" in q
        ):

            if (
                "Region" in dashboard_df.columns
                and "Sales" in dashboard_df.columns
            ):

                region_sales = (
                    dashboard_df
                    .groupby("Region")["Sales"]
                    .sum()
                    .sort_values(
                        ascending=False
                    )
                )

                if not region_sales.empty:

                    top_region = (
                        region_sales.index[0]
                    )

                    top_value = (
                        region_sales.iloc[0]
                    )

                    st.success(
                        f"🌍 Top Region: "
                        f"{top_region}"
                    )

                    st.write(
                        f"Total Sales: "
                        f"**{top_value:,.2f}**"
                    )

            else:

                st.warning(
                    "Region or Sales column "
                    "not found."
                )

        # -------------------------------------------------
        # AVERAGE QUANTITY
        # -------------------------------------------------

        elif "average quantity" in q:

            if "Quantity" in dashboard_df.columns:

                average_quantity = (
                    dashboard_df["Quantity"]
                    .mean()
                )

                st.success(
                    f"📦 Average Quantity: "
                    f"{average_quantity:,.2f}"
                )

            else:

                st.warning(
                    "Quantity column not found."
                )

        # -------------------------------------------------
        # TOTAL QUANTITY
        # -------------------------------------------------

        elif "total quantity" in q:

            if "Quantity" in dashboard_df.columns:

                total_quantity = (
                    dashboard_df["Quantity"]
                    .sum()
                )

                st.success(
                    f"📦 Total Quantity: "
                    f"{total_quantity:,.0f}"
                )

            else:

                st.warning(
                    "Quantity column not found."
                )

        # -------------------------------------------------
        # ROW COUNT
        # -------------------------------------------------

        elif (
            "number of rows" in q
            or "how many rows" in q
            or "number of records" in q
        ):

            st.success(
                f"📋 Number of Records: "
                f"{len(dashboard_df):,}"
            )

        # -------------------------------------------------
        # COLUMN COUNT
        # -------------------------------------------------

        elif "number of columns" in q:

            st.success(
                f"📊 Number of Columns: "
                f"{len(dashboard_df.columns):,}"
            )

        # -------------------------------------------------
        # MISSING VALUES
        # -------------------------------------------------

        elif (
            "missing values" in q
            or "missing data" in q
        ):

            missing = (
                dashboard_df
                .isnull()
                .sum()
                .sum()
            )

            st.success(
                f"🔍 Missing Values: "
                f"{missing:,}"
            )

        # -------------------------------------------------
        # UNKNOWN QUESTION
        # -------------------------------------------------

        else:

            st.info(
                "🤔 I don't understand "
                "that question yet."
            )

            st.write(
                "Try asking:"
            )

            st.write(
                "• What is the total sales?"
            )

            st.write(
                "• Which product has "
                "the highest sales?"
            )

            st.write(
                "• Which region has "
                "the highest sales?"
            )

            st.write(
                "• What is the average quantity?"
            )

            st.write(
                "• What is the total quantity?"
            )

            st.write(
                "• How many rows are there?"
            )

# =========================================================
# EMPTY STATE
# =========================================================

else:

    st.info(
        "👆 Upload a CSV file above to start "
        "analyzing your data."
    )

    st.write(
        "### 🚀 What you can do"
    )

    empty1, empty2, empty3 = st.columns(3)

    with empty1:

        st.write("📊 **Explore Data**")
        st.caption(
            "Preview your dataset and "
            "understand its structure."
        )

    with empty2:

        st.write("📈 **Analyze Trends**")
        st.caption(
            "Discover patterns using "
            "interactive charts."
        )

    with empty3:

        st.write("💡 **Find Insights**")
        st.caption(
            "Automatically identify "
            "important business insights."
        )