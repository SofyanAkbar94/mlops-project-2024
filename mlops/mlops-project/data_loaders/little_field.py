if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader


# Print to check if the path exists
model_dir = '/home/src/mlruns/0/bff065e2e4404b1295fafaf075d5c424/artifacts'
print(f"Contents of {model_dir}: {os.listdir(model_dir)}")



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'