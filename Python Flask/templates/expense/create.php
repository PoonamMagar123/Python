<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>Add Data</title>
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <h4>Add Expense  
                            <a href="<?= base_url('expense')?>" class="btn btn-danger float-right">Back</a>
                        </h4>
                    </div>
                    <div class="card-body">
                    <form action="<?= base_url('expense_store') ?>" method="post" enctype="multipart/form-data">
   
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group mb-3">
                                        <label for="name">Name</label>
                                        <input type="text" name="name" id="name" class="form-control" placeholder="Enter Name" required>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group mb-3">
                                        <label for="phone">Phone</label>
                                        <input type="number" name="phone" id="phone" class="form-control" placeholder="Enter Phone Number" required>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group mb-3">
                                        <label for="photo">Upload Photo</label>
                                        <input type="file" name="photo" id="file_photo" class="form-control" accept="image/*" required>
                                    </div>
                                </div>
                                

                                <div class="col-md-6">
                                    <div class="form-group mb-3">
                                        <label for="amount">Amount</label>
                                        <input type="number" name="amount" id="amount" class="form-control" placeholder="Enter Amount" oninput="calculateTotalExpense()" >
                                    </div>
                                </div>
                                
                                <div class="col-md-6">
                                    <div class="form-group mb-3">
                                        <label for="expense">Expense</label>
                                        <input type="text" name="expense" id="expense" class="form-control" placeholder="Enter Expense" oninput="calculateTotalExpense()" >
                                    </div>
                                </div>
                                
                                <div class="col-md-6">
                                    <div class="form-group mb-3">
                                        <label for="total_expense">Total Expense</label>
                                        <input type="number" name="total_expense" id="totalExpense" class="form-control" placeholder="Enter Total Expense" readonly>
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <div class="form-group">
                                        <button type="submit" class="btn btn-primary px-4">Save Expense</button>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
<!-- JavaScript code -->
<script>
    function calculateTotalExpense() {
        // Get the values of amount and expense
        var amount = parseFloat(document.getElementById('amount').value) || 0;
        var expense = parseFloat(document.getElementById('expense').value) || 0;

        // Calculate total expense
        var totalExpense = amount - expense;

        // Update the total expense field
        document.getElementById('totalExpense').value = totalExpense;
    }
</script>
