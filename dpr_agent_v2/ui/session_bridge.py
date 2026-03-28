"""
ui/session_bridge.py
"""

import asyncio
import concurrent.futures
import streamlit as st
from agents.orchestrator import Orchestrator


def get_orchestrator(api_key: str) -> Orchestrator:
    if "orchestrator" not in st.session_state or \
       st.session_state.get("orchestrator_key") != api_key:
        st.session_state.orchestrator     = Orchestrator(api_key)
        st.session_state.orchestrator_key = api_key
    return st.session_state.orchestrator


def run_async(coro):
    def _run(c):
        return asyncio.run(c)

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(_run, coro)
        return future.result()
