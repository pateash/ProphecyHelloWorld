export PROPHECY_PAT=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxLUtqdEp1eVpMQmhPV3QwQmxrTWxVZkFWM0k1Q01sNmwwSmg5N1FSUUYwNlRWcVY5NEhqc05HSFRyZzl3b3dsZG1zNmdyaDV2SUJmTER6RldCSWFvODYzbXo1OGc5ZDhKV1ljdURnVXpDVis0R1wvSGtUUExFPSIsImlzcyI6ImFwcF9zYWFzIiwiZXhwIjoxNzQ1MDY3MzU1LCJpYXQiOjE3MzA4MTQ5NTUsImp0aSI6IjNiNmE0Y2NlNDEyYmY5NjFkY2RiZDMxOWM3MzdjOTJjMmIwNThmNzU1OGJhZGE2NzcxYThhM2ZmZmFmY2YwMjZkMjk2NmUxYzc3OTA4MjA0MmMwNzIwNmQ5OTdkOTJlZGYwZmM1ZmRhODUzMTNiNDU0NmIxNzc1MjllMjY4YmI3YzQ0MDNhYTRjM2FlNmY5NjM2YWJlMzk0ZjM5MzQzY2Y3NmUxNWQwYmVkNGFlYjBlYmJjMDVlODIxYjc4YzgzODhmOWU4MDBjZWQ3MGNhZmI5MjRmZmE3ZDZlM2QyY2U5YzRmMGY4OTdiZjNhNmYzYTA2ZTVhMjNiNDdmNTk5YmIifQ.Bq4F-_BuZdDtjCKXi28lSCy1T1w__3Vf_PyYr6Ll3V0
export PROPHECY_URL=https://app.prophecy.io
pip install -U prophecy-lineage-extractor==0.11.0.dev2
if [[ $? != 0 ]];then
  echo "Error in installing package"
  exit 1
fi
OUTPUT_DIR="output"
python -m prophecy_lineage_extractor --project-id 36587 --pipeline-id 36587/pipelines/customer_orders_demo --output-dir $OUTPUT_DIR

GIT_COMMIT="1"
if [[ $GIT_COMMIT == "1" ]]; then
    echo "Commiting enabled, adding output file"
    git add $OUTPUT_DIR/*
    echo "========================================"
    git commit -m "Adding output file"
    echo "========================================"
    echo "Pushing changes"
    git push
else
    # simple version are created manually from code edits.
    echo "Commiting to git is not enabled"
fi
