
echo "Build Started"
python3.9 manage.py collectstatic --noinput --clear
echo "Build End!"